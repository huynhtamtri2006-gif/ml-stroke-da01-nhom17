param(
    [string]$LuanUsername = '',
    [switch]$Execute
)
$ErrorActionPreference = 'Stop'
$Repository = 'huynhtamtri2006-gif/ml-stroke-da01-nhom17'
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$TaskPath = Join-Path $ProjectRoot 'docs/tasks/task_manifest.csv'
$Tasks = @(Import-Csv -LiteralPath $TaskPath -Encoding UTF8)
if (-not $Execute) {
    $Tasks | Select-Object task_id, owner, start_date, title | Format-Table -Wrap
    Write-Output 'DRY RUN: không tạo tài nguyên GitHub. Khi sẵn sàng, thêm -Execute; username Luân có thể để trống để chưa gán.'
    exit 0
}
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'Cần cài gh và đăng nhập bằng tài khoản của chính bạn.' }
$RepoRaw = & gh repo view $Repository --json nameWithOwner,visibility
if ($LASTEXITCODE -ne 0) { throw 'Không đọc được repository; kiểm tra đăng nhập/quyền/repo đã tạo.' }
$RepoState = $RepoRaw | ConvertFrom-Json
if ($RepoState.nameWithOwner -ne $Repository -or $RepoState.visibility -ne 'PRIVATE') { throw 'Chỉ nhập vào đúng repository Private đã chỉ định.' }
$ExistingRaw = & gh issue list --repo $Repository --state all --limit 1000 --json number,title,url
if ($LASTEXITCODE -ne 0) { throw 'Không đọc được Issue đang có; dừng để tránh tạo trùng.' }
$Existing = @($ExistingRaw | ConvertFrom-Json)
$MilestoneRaw = & gh api --paginate "repos/$Repository/milestones?state=all&per_page=100" --jq '.[].title'
if ($LASTEXITCODE -ne 0) { throw 'Không đọc được milestone.' }
$MilestoneNames = @($MilestoneRaw)
foreach ($M in @($Tasks.milestone | Sort-Object -Unique)) {
    if ($M -notin $MilestoneNames) {
        & gh api --method POST "repos/$Repository/milestones" -f "title=$M" --silent
        if ($LASTEXITCODE -ne 0) { throw "Không tạo được milestone $M" }
    }
}
$Map = @()
foreach ($Task in $Tasks) {
    $Prefix = '[' + $Task.task_id + '] '
    $Found = @($Existing | Where-Object { $_.title.StartsWith($Prefix) })
    if ($Found.Count -gt 1) { throw "Có nhiều Issue cho $($Task.task_id), kiểm tra tay." }
    if ($Found.Count -eq 1) {
        $Url = $Found[0].url
    } else {
        $BodyPath = Join-Path $ProjectRoot ("docs/issues/" + $Task.task_id + '.md')
        $GhArgs = @('issue','create','--repo',$Repository,'--title',$Task.title,'--body-file',$BodyPath,'--milestone',$Task.milestone)
        $Assignee = if ($Task.person -eq 'tri') { 'huynhtamtri2006-gif' } else { $LuanUsername }
        if (-not [string]::IsNullOrWhiteSpace($Assignee)) { $GhArgs += @('--assignee',$Assignee) }
        $Url = & gh @GhArgs
        if ($LASTEXITCODE -ne 0) { throw "Không tạo được $($Task.task_id); sửa lỗi rồi chạy lại, Issue trước đó được nhận diện qua prefix." }
        $Url = ($Url | Select-Object -Last 1).Trim()
    }
    $Map += [PSCustomObject]@{task_id=$Task.task_id;url=$Url;planned_owner=$Task.owner}
    $Map | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $ProjectRoot 'docs/tasks/issue_map.json') -Encoding UTF8
    Write-Output "$($Task.task_id) $Url"
}
Write-Output 'Đã xử lý danh mục Issue. Thêm Issue vào Project và điền custom fields theo PROJECTS_SETUP.md; script chưa tạo Project/view hoặc custom fields.'
