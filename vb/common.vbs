Option Explicit

Function GetOptionValue(name, optStartPos)
    Dim args
    Dim lastIdx
    Dim i
    Dim arg
    
    Set args = WScript.Arguments
    lastIdx = args.Count - 1
    If optStartPos > lastIdx Then
        GetOptionValue = ""
        Exit Function
    Else
        For i = optStartPos To lastIdx
            arg = args(i)
            If arg = name Then
                If i + 1 < args.Count Then
                    GetOptionValue = args(i + 1)
                Else
                    GetOptionValue = ""
                End If
                Exit Function
            End If
        Next
    End If

    GetOptionValue = ""
End Function

Function GetLogDatetime()

    Dim curDate
    Dim ymdhms
    Dim curTime
    Dim ms
    Dim retVal

    curDate = Now()
    curTime = Timer()

    ymdhms = Year(curDate) & "-" & Right("0" & Month(curDate), 2) & "-" & Right("0" & Day(curDate), 2) & _
        " " & Right("0" & Hour(curDate), 2) & ":" & Right("0" & Minute(curDate), 2) & ":" & Right("0" & Second(curDate), 2)
    ms = Right("000" & Fix((curTime - Fix(curTime)) * 1000), 3)

    retVal = ymdhms & "." & ms

    GetLogDatetime = retVal

End Function

Sub Log(msg)
    WScript.echo(GetLogDatetime() + vbTab + msg)
End Sub
