WinActivate("文件上传");
ControlSetText("文件上传", "", "Edit1", $CmdLine[1]);
Sleep(8000);
ControlClick("文件上传", "", "Button1");
