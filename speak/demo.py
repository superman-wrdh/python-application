# import win32com.client
#
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("我是语音助手 小白，what can I do for you ?")
from win32com.client import constants
import os
import win32com.client
import pythoncom

speaker = win32com.client.Dispatch("SAPI.SPVOICE")


class SpeechRecognition:
    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule", constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule", 1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")

    def say(self, phrase):
        self.speaker.Speak(phrase)


class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("你在说 ", newResult.PhraseInfo.GetText())
        speechstr = newResult.PhraseInfo.GetText()
        # 下面即为语音识别信息对应,打开响应操作
        if speechstr == "记事本":
            os.system('notepad')
        elif speechstr == "写字板":
            os.system('write')
        elif speechstr == "画图板":
            os.system('mspaint')
        else:
            pass


if __name__ == '__main__':

    speaker.Speak("语音识别开启")
    wordsToAdd = ["记事本", "写字板", "画图板", ]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()
