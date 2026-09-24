param([string]$Source, [string]$Class, [string]$Args2)
$S = Split-Path -Parent $MyInvocation.MyCommand.Path
[Environment]::CurrentDirectory = $S
Set-Location $S
$src = Get-Content (Join-Path $S $Source) -Raw
$src = $src -replace "(?m)^class $Class", "public class $Class" -replace 'static void Main', 'public static void Main'
$cp = New-Object System.CodeDom.Compiler.CompilerParameters
$cp.CompilerOptions = '/optimize+ /platform:x64'
$cp.GenerateInMemory = $true
[void]$cp.ReferencedAssemblies.Add('System.dll')
[void]$cp.ReferencedAssemblies.Add('System.Core.dll')
[void]$cp.ReferencedAssemblies.Add('System.Numerics.dll')
Add-Type -TypeDefinition $src -Language CSharp -CompilerParameters $cp
$t = [Diagnostics.Stopwatch]::StartNew()
([type]$Class)::Main([string[]]($Args2 -split " "))
"elapsed {0:F1}s" -f $t.Elapsed.TotalSeconds
