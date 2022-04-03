Option Explicit

Execute CreateObject("Scripting.FileSystemObject").OpenTextFile("common.vbs").ReadAll()

Dim args
Dim ip
Dim user
Dim password
Dim collect_path

Set args = WScript.Arguments

Log("Start XXX.")

If args.Count < 4 Then
    Log("required error")
    WScript.Quit(222)
End If

ip = args(0)
user = args(1)
password = args(2)
collect_path = args(3)

WScript.echo(ip)
WScript.echo(user)
WScript.echo(password)
WScript.echo(collect_path)

Log("End XXX.")
