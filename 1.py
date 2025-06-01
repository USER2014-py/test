from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle
import arabic_reshaper
from bidi.algorithm import get_display
import vlc
import time
class BackgroundFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.bg = Rectangle(source='F:/My IMAGES/1.png', pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def change_background(self, new_image):
        self.bg.source = new_image
        self.update_bg()
    
def to_arabic_number(number):
    arabic_digits = {
        '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
        '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩',
    }
    return ''.join(arabic_digits.get(d, d) for d in str(number))


class Az(App):
    def click_sw(self, instance):
        self.layout.change_background(self.SW[0])
        self.layout.clear_widgets()
        self.layout.add_widget(self.BAK)
        self.layout.add_widget(self.SETS)
        self.layout.add_widget(self.U)
        self.layout.add_widget(self.N)
        self.sad = 0
        self.SETS.text=to_arabic_number(self.SAD[0])
        self.A = 'SW'

    def click_ss(self, instance):
        self.layout.change_background("F:/My IMAGES/SS.png")
        self.layout.clear_widgets()
        self.layout.add_widget(self.BAK)
        self.layout.add_widget(self.PLAYS)
        self.layout.add_widget(self.Speed)
        self.A = 'SS'
        self.PLAYS.color=(0, 1, 0, 1)
        self.PLAYS.text=self.play_S_1_text
        
    def click_ms(self, instance):
        self.layout.change_background("F:/My IMAGES/MS.png")
        self.layout.clear_widgets()
        self.layout.add_widget(self.BAK)
        self.layout.add_widget(self.PLAYS)
        self.layout.add_widget(self.Speed)
        self.A = 'MS'
        self.PLAYS.color=(0, 1, 0, 1)
        self.PLAYS.text=self.play_S_1_text

    def click_mw(self, instance):
        self.layout.change_background(self.MW[0])
        self.layout.clear_widgets()
        self.layout.add_widget(self.BAK)
        self.layout.add_widget(self.Um)
        self.layout.add_widget(self.Nm)
        self.layout.add_widget(self.SETM)
        self.mad = 0
        self.A = 'MS'
        self.PLAYS.color=(0, 1, 0, 1)
        self.PLAYS.text=self.play_S_1_text

    def click_bk(self, instance):
        if self.A == 'SS':
            self.S1.stop()
        if self.A == 'MS':
            self.M1.stop()
        if self.A == 'SB':
            self.SPSS.stop()
        if self.A == 'ST':
            self.STSS.stop()
        if self.A == 'T':
            self.TSS.stop()
        self.layout.change_background("F:/My IMAGES/1.png")
        self.layout.clear_widgets()
        self.layout.add_widget(self.SWB)
        self.layout.add_widget(self.SSB)
        self.layout.add_widget(self.MWB)
        self.layout.add_widget(self.MSB)
        self.layout.add_widget(self.SB)
        self.layout.add_widget(self.ST)
        self.layout.add_widget(self.T)
        self.A = '0'
        
    def click_sb(self, instance):
        self.layout.change_background("F:\My IMAGES\SB.png")
        self.layout.clear_widgets()
        self.layout.add_widget(self.BAK)
        self.layout.add_widget(self.PLAYS)
        self.layout.add_widget(self.Speed)
        self.A = 'SB'
        self.PLAYS.color=(0, 1, 0, 1)
        self.PLAYS.text=self.play_S_1_text
        
    def click_st(self, instance):
        self.layout.change_background("F:\My IMAGES\ST.png")
        self.layout.clear_widgets()
        self.layout.add_widget(self.BAK)
        self.layout.add_widget(self.PLAYS)
        self.layout.add_widget(self.Speed)
        self.A = 'ST'
        self.PLAYS.color=(0, 1, 0, 1)
        self.PLAYS.text=self.play_S_1_text
        
    def click_t(self, instance):
        self.layout.change_background("F:\My IMAGES\T.png")
        self.layout.clear_widgets()
        self.layout.add_widget(self.BAK)
        self.layout.add_widget(self.PLAYS)
        self.layout.add_widget(self.Speed)
        self.A = 'T'
        self.PLAYS.color=(0, 1, 0, 1)
        self.PLAYS.text=self.play_S_1_text

        

    def click_sts(self, instance):
        self.current_value = int(instance.text)
        if self.current_value == 1:
            self.sad += 1
            if self.sad < len(self.SAD):
                self.SETS.text = to_arabic_number(str(self.SAD[self.sad]))
                self.layout.change_background(self.SW[self.sad])
        else:
        # إذا النص ليس 1، ننقص النص (في الزر) واحدًا فقط بدون تغيير العداد أو الخلفية
            new_value = self.current_value - 1
            if new_value < 1:
                new_value = 1  # لا تقل عن 1
            self.SETS.text = to_arabic_number(str(new_value))
    
    def click_U(self, instance):
        if self.sad != 25:
            if self.sad + 1 < len(self.SAD):
                self.sad += 1
                self.layout.change_background(self.SW[self.sad])
                self.SETS.text = to_arabic_number(str(self.SAD[self.sad]))
            
    def click_N(self, instance):
        if self.sad != 0:
            if self.sad - 1 < len(self.SAD):
                self.sad -= 1
                self.layout.change_background(self.SW[self.sad])
                self.SETS.text = to_arabic_number(str(self.SAD[self.sad]))

    def click_stm(self, instance):
        self.current_value2 = int(instance.text)
        if self.current_value2 == 1:
            self.mad += 1
            if self.mad < len(self.MAD):
                self.SETM.text = to_arabic_number(str(self.MAD[self.mad]))
                self.layout.change_background(self.MW[self.mad])
        else:
        # إذا النص ليس 1، ننقص النص (في الزر) واحدًا فقط بدون تغيير العداد أو الخلفية
            new_value2 = self.current_value2 - 1
            if new_value2 < 1:
                new_value2 = 1  # لا تقل عن 1
            self.SETM.text = to_arabic_number(str(new_value2))
    
    def click_Um(self, instance):
        if self.mad != 23:
            if self.mad + 1 < len(self.MAD):
                self.mad += 1
                self.layout.change_background(self.MW[self.mad])
                self.SETM.text = to_arabic_number(str(self.MAD[self.mad]))
            
    def click_Nm(self, instance):
        if self.mad > 0:
            if self.mad - 1 < len(self.MAD):
                self.mad -= 1
                self.layout.change_background(self.MW[self.mad])
                self.SETM.text = to_arabic_number(str(self.MAD[self.mad]))
    def click_pl_S(self, instance):
        self.MHMS = 1
        if self.A == 'SS':
            self.S1.play()
            self.layout.clear_widgets()
            self.layout.add_widget(self.BAK)
            self.layout.add_widget(self.Speed)
            self.layout.add_widget(self.KS)
            self.layout.add_widget(self.tenup)
            self.layout.add_widget(self.tendn)
        if self.A == 'MS':
           self.M1.play()
           self.layout.clear_widgets()
           self.layout.add_widget(self.BAK)
           self.layout.add_widget(self.Speed)
           self.layout.add_widget(self.KS)
           self.layout.add_widget(self.tenup)
           self.layout.add_widget(self.tendn)
        if self.A == 'SB':
           self.SPSS.play()
           self.layout.clear_widgets()
           self.layout.add_widget(self.BAK)
           self.layout.add_widget(self.Speed)
           self.layout.add_widget(self.KS)
           self.layout.add_widget(self.tenup)
           self.layout.add_widget(self.tendn)
        if self.A == 'ST':
           self.STSS.play()
           self.layout.clear_widgets()
           self.layout.add_widget(self.BAK)
           self.layout.add_widget(self.Speed)
           self.layout.add_widget(self.KS)
           self.layout.add_widget(self.tenup)
           self.layout.add_widget(self.tendn)
        if self.A == 'T':
           self.TSS.play()
           self.layout.clear_widgets()
           self.layout.add_widget(self.BAK)
           self.layout.add_widget(self.Speed)
           self.layout.add_widget(self.KS)
           self.layout.add_widget(self.tenup)
           self.layout.add_widget(self.tendn)
           
    def K_S_1(self, instance):
        self.MHMS = 0
        if self.A == 'SS':
            self.S1.pause()
            self.layout.clear_widgets()
            self.layout.add_widget(self.PLAYS)
            self.layout.add_widget(self.BAK)
            self.layout.add_widget(self.Speed)
            self.PLAYS.color=(0.5, 0.5, 0, 1)
            self.PLAYS.text=self.I_S_1_text
        if self.A == 'MS':
           self.M1.pause()
           self.layout.clear_widgets()
           self.layout.add_widget(self.BAK)
           self.layout.add_widget(self.Speed)
           self.layout.add_widget(self.PLAYS)
           self.PLAYS.color=(0.5, 0.5, 0, 1)
           self.PLAYS.text=self.I_S_1_text
        if self.A == 'SB':
           self.SPSS.pause()
           self.layout.clear_widgets()
           self.layout.add_widget(self.BAK)
           self.layout.add_widget(self.Speed)
           self.layout.add_widget(self.PLAYS)
           self.PLAYS.color=(0.5, 0.5, 0, 1)
           self.PLAYS.text=self.I_S_1_text
        if self.A == 'ST':
           self.STSS.pause()
           self.layout.clear_widgets()
           self.layout.add_widget(self.BAK)
           self.layout.add_widget(self.Speed)
           self.layout.add_widget(self.PLAYS)
           self.PLAYS.color=(0.5, 0.5, 0, 1)
           self.PLAYS.text=self.I_S_1_text
        if self.A == 'T':
           self.TSS.pause()
           self.layout.clear_widgets()
           self.layout.add_widget(self.BAK)
           self.layout.add_widget(self.Speed)
           self.layout.add_widget(self.PLAYS)
           self.PLAYS.color=(0.5, 0.5, 0, 1)
           self.PLAYS.text=self.I_S_1_text

    def speednot(self, instance):
        if self.sn == 0:
            self.layout.clear_widgets()
            self.layout.add_widget(self.Speed05)
            self.layout.add_widget(self.Speed075)
            self.layout.add_widget(self.Speed1)
            self.layout.add_widget(self.Speed2)
            self.layout.add_widget(self.Speed3)
            self.layout.add_widget(self.Speed)
            self.layout.add_widget(self.BAK)
    def speed1(self, instance):
        if self.A == 'SS':
            self.S1.set_rate(1)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'MS':
            self.M1.set_rate(1)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'SB':
            self.SPSS.set_rate(1)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'ST':
            self.STSS.set_rate(1)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'T':
            self.TSS.set_rate(1)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
    def speed05(self, instance):
        if self.A == 'SS':
            self.S1.set_rate(0.5)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'MS':
            self.M1.set_rate(0.5)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'SB':
            self.SPSS.set_rate(0.5)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'ST':
            self.STSS.set_rate(0.5)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'T':
            self.TSS.set_rate(0.5)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
    def speed075(self, instance):
        if self.A == 'SS':
            self.S1.set_rate(0.75)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'MS':
            self.M1.set_rate(0.75)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'SB':
            self.SPSS.set_rate(0.75)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'ST':
            self.STSS.set_rate(0.75)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'T':
            self.TSS.set_rate(0.75)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
    def speed2(self, instance):
        if self.A == 'SS':
            self.S1.set_rate(2)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'MS':
            self.M1.set_rate(2)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'SB':
            self.SPSS.set_rate(2)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'ST':
            self.STSS.set_rate(2)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'T':
            self.TSS.set_rate(2)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
                
                
                
    def speed3(self, instance):
        if self.A == 'SS':
            self.S1.set_rate(3)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'MS':
            self.M1.set_rate(3)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'SB':
            self.SPSS.set_rate(3)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'ST':
            self.STSS.set_rate(3)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
        if self.A == 'T':
            self.TSS.set_rate(3)
            if self.MHMS == 0:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.PLAYS)
            else:
                self.layout.clear_widgets()
                self.layout.add_widget(self.BAK)
                self.layout.add_widget(self.Speed)
                self.layout.add_widget(self.KS)
                self.layout.add_widget(self.tenup)
                self.layout.add_widget(self.tendn)
                
                
    def Tenup(self, inctance):
        if self.A == 'SS':
            current_time = self.S1.get_time()
            self.S1.set_time(current_time + 10000)
        if self.A == 'MS':
            current_time = self.M1.get_time()
            self.M1.set_time(current_time + 10000)
        if self.A == 'SB':
            current_time = self.SPSS.get_time()
            self.SPSS.set_time(current_time + 10000)
        if self.A == 'ST':
            current_time = self.STSS.get_time()
            self.STSS.set_time(current_time + 10000)
        if self.A == 'T':
            current_time = self.TSS.get_time()
            self.TSS.set_time(current_time + 10000)
            
    def Tendn(self, inctance):
        if self.A == 'SS':
            current_time = self.S1.get_time()
            self.S1.set_time(current_time - 10000)
        if self.A == 'MS':
            current_time = self.M1.get_time()
            self.M1.set_time(current_time - 10000)
        if self.A == 'SB':
            curret_time = self.SPSS.get_time()
            self.SPSS.set_time(curret_time - 10000)
        if self.A == 'ST':
            current_time = self.STSS.get_time()
            self.STSS.set_time(current_time - 10000)
        if self.A == 'T':
            current_time = self.TSS.get_time()
            self.TSS.set_time(current_time - 10000)

    def build(self):
        self.sp = 0
        self.sn = 0
        self.snn = 0
        self.S1 = vlc.MediaPlayer(r"F:\MY SOUNDS\اذكار الصباح\اذكار الصباح.mp3")
        self.M1 = vlc.MediaPlayer(r"F:\MY SOUNDS\اذكار المساء\اذكار المساء.mp3")
        self.TSS = vlc.MediaPlayer(r"F:\MY SOUNDS\ff\1.mp3")
        self.STSS = vlc.MediaPlayer("F:\MY SOUNDS\استغفر الله واتوب اليه\أستغفر الله وأتوب إليه 100 مرة مشاري العفاسي.mp3")
        self.SPSS = vlc.MediaPlayer("F:\MY SOUNDS\استغفر\سبحان الله وبحمده 100 مرة بصوت مشاري العفاسي.mp3")
        self.MHMS = 0
        self.sad = 0
        self.mad = 0
        self.layout = BackgroundFloatLayout()
        self.buttonSW_text = get_display(arabic_reshaper.reshape('اذكار الصباح كتابةً'))
        self.buttonSS_text = get_display(arabic_reshaper.reshape('اذكار الصباح صوتا'))
        self.buttonMW_text = get_display(arabic_reshaper.reshape('اذكار المساء كتابةً'))
        self.buttonMS_text = get_display(arabic_reshaper.reshape('اذكار المساء صوتا'))
        self.buttonBK_text = get_display(arabic_reshaper.reshape('رجوع'))
        self.SET_text     = get_display(arabic_reshaper.reshape('العادية'))
        self.play_S_1_text     = get_display(arabic_reshaper.reshape('تشغيل'))
        self.K_S_1_text     = get_display(arabic_reshaper.reshape('ايقاف'))
        self.I_S_1_text     = get_display(arabic_reshaper.reshape('استئناف'))
        self.T_text = get_display(arabic_reshaper.reshape('تاج الذكر'))
        self.ST_text = get_display(arabic_reshaper.reshape('استغفر الله واتوب اليه'))
        self.SB_text = get_display(arabic_reshaper.reshape('سبحان الله وبحمده'))
        self.T_text = get_display(arabic_reshaper.reshape('تاج الذكر'))
        self.speed_text = get_display(arabic_reshaper.reshape('السرعة'))

        self.MAD = [1, 1, 3, 3, 3, 1, 1, 1, 4, 1, 3, 7, 1, 1, 3, 3, 1, 1, 1, 1, 10, 100, 3, 10]
        self.SAD = [1, 1, 3, 3, 3, 1, 1, 1, 4, 1, 3, 7, 1, 1, 3, 3, 1, 1, 1, 100, 10, 100, 3, 1, 100, 10]

        self.SW = [
            "F:/My IMAGES/الصباح/1.png",  "F:/My IMAGES/الصباح/2.png",  "F:/My IMAGES/الصباح/3.png",
            "F:/My IMAGES/الصباح/4.png",  "F:/My IMAGES/الصباح/5.png",  "F:/My IMAGES/الصباح/6.png",
            "F:/My IMAGES/الصباح/7.png",  "F:/My IMAGES/الصباح/8.png",  "F:/My IMAGES/الصباح/9.png",
            "F:/My IMAGES/الصباح/10.png", "F:/My IMAGES/الصباح/11.png", "F:/My IMAGES/الصباح/12.png",
            "F:/My IMAGES/الصباح/13.png", "F:/My IMAGES/الصباح/14.png", "F:/My IMAGES/الصباح/15.png",
            "F:/My IMAGES/الصباح/16.png", "F:/My IMAGES/الصباح/17.png", "F:/My IMAGES/الصباح/18.png",
            "F:/My IMAGES/الصباح/19.png", "F:/My IMAGES/الصباح/20.png", "F:/My IMAGES/الصباح/21.png",
            "F:/My IMAGES/الصباح/22.png", "F:/My IMAGES/الصباح/23.png", "F:/My IMAGES/الصباح/24.png",
            "F:/My IMAGES/الصباح/25.png", "F:/My IMAGES/الصباح/26.png"
        ]

        self.MW = [
            "F:/My IMAGES/المساء/1.png",   "F:/My IMAGES/المساء/2.png",   "F:/My IMAGES/المساء/3.png",
            "F:/My IMAGES/المساء/4.png",   "F:/My IMAGES/المساء/5.png",   "F:/My IMAGES/المساء/6.png",
            "F:/My IMAGES/المساء/7.png",   "F:/My IMAGES/المساء/8.png",   "F:/My IMAGES/المساء/9.png",
            "F:/My IMAGES/المساء/10.png",  "F:/My IMAGES/المساء/11.png",  "F:/My IMAGES/المساء/12.png",
            "F:/My IMAGES/المساء/13.png",  "F:/My IMAGES/المساء/14.png",  "F:/My IMAGES/المساء/15.png",
            "F:/My IMAGES/المساء/16.png",  "F:/My IMAGES/المساء/17.png",  "F:/My IMAGES/المساء/18.png",
            "F:/My IMAGES/المساء/19.png",  "F:/My IMAGES/المساء/20.png",  "F:/My IMAGES/المساء/21.png",
            "F:/My IMAGES/المساء/22.png",  "F:/My IMAGES/المساء/23.png",  "F:/My IMAGES/المساء/24.png"
        ]

        self.A = '0'

        self.SWB = Button(
            text=self.buttonSW_text,
            font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.7},
        )
        self.SWB.bind(on_release=self.click_sw)

        self.SSB = Button(
            text=self.buttonSS_text,
            font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.640}
        )
        self.SSB.bind(on_release=self.click_ss)

        self.MWB = Button(
            text=self.buttonMW_text,
            font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.580}
        )
        self.MWB.bind(on_release=self.click_mw)

        self.MSB = Button(
            text=self.buttonMS_text,
            font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.520}
        )
        self.MSB.bind(on_release=self.click_ms)
        
        self.SB = Button(
            text=self.SB_text,
            font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.460}
        )
        self.SB.bind(on_release=self.click_sb)
        
        self.ST = Button(
            text=self.ST_text,
            font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.400}
        )
        self.ST.bind(on_release=self.click_st)
        
        self.T = Button(
            text=self.T_text,
            font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.340}
        )
        self.T.bind(on_release=self.click_t)

        self.BAK = Button(
            text=self.buttonBK_text,
            font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.9, 'center_y': 0.96}
        )
        self.BAK.bind(on_release=self.click_bk)

        self.SETS = Button(
            text=to_arabic_number(str(self.SAD[self.sad])), font_name='F:/My FONTS/Amiri.ttf', font_size=90,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )
        self.SETS.bind(on_release=self.click_sts)
        
        self.U = Button(
            text='<', font_name='F:/My FONTS/Amiri.ttf', font_size=55,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.05, 'center_y': 0.5}
        )
        self.U.bind(on_release=self.click_U)
        
        self.N = Button(
            text='>', font_name='F:/My FONTS/Amiri.ttf', font_size=55,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.95, 'center_y': 0.5}
        )
        self.N.bind(on_release=self.click_N)
  
        self.SETM = Button(
            text=to_arabic_number(str(self.SAD[self.sad])), font_name='F:/My FONTS/Amiri.ttf', font_size=90,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )
        self.SETM.bind(on_release=self.click_stm)
        
        self.Um = Button(
            text='<', font_name='F:/My FONTS/Amiri.ttf', font_size=55,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.05, 'center_y': 0.5}
        )
        self.Um.bind(on_release=self.click_Um)
        
        self.Nm = Button(
            text='>', font_name='F:/My FONTS/Amiri.ttf', font_size=55,
            color=(0.7, 0.3, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.95, 'center_y': 0.5}
        )
        self.Nm.bind(on_release=self.click_Nm)
        
        self.PLAYS = Button(
            text=self.play_S_1_text, font_name='F:/My FONTS/Amiri.ttf', font_size=90,
            color=(0, 1, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.675}
        )
        self.PLAYS.bind(on_release=self.click_pl_S)
        
        
        self.KS = Button(
            text=self.K_S_1_text, font_name='F:/My FONTS/Amiri.ttf', font_size=90,
            color=(1, 0, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.675}
        )
        self.KS.bind(on_release=self.K_S_1)
        
        self.Speed = Button(
            text=self.speed_text, font_name='F:/My FONTS/Amiri.ttf', font_size=35,
            color=(0.7, 0.35, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.15, 'center_y': 0.05}
            )
        self.Speed.bind(on_release=self.speednot)
        
        self.Speed05 = Button(
            text=str(to_arabic_number(0.5)), font_name='F:/My FONTS/Amiri.ttf', font_size=35,
            color=(1, 0, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.15, 'center_y': 0.12}
            )
        self.Speed05.bind(on_release=self.speed05)
        self.Speed075 = Button(
            text=str(to_arabic_number(0.75)), font_name='F:/My FONTS/Amiri.ttf', font_size=35,
            color=(0.75, 0.25, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.15, 'center_y': 0.17}
            )
        self.Speed075.bind(on_release=self.speed075)
        self.Speed1 = Button(
            text=str(to_arabic_number(1) + self.SET_text), font_name='F:/My FONTS/Amiri.ttf', font_size=35,
            color=(0.5, 0.5, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.15, 'center_y': 0.22}
            )
        self.Speed1.bind(on_release=self.speed1)
        self.Speed2 = Button(
            text=str(to_arabic_number(2)), font_name='F:/My FONTS/Amiri.ttf', font_size=35,
            color=(0.25, 0.75, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.15, 'center_y': 0.27}
            )
        self.Speed2.bind(on_release=self.speed2)
        self.Speed3 = Button(
            text=str(to_arabic_number(3)), font_name='F:/My FONTS/Amiri.ttf', font_size=35,
            color=(0, 1, 0, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.15, 'center_y': 0.32}
            )
        
        self.tenup = Button(
            text='>' + to_arabic_number(10), font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.5, 1, 0.5, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.9, 'center_y': 0.675}
            )
        
        self.tendn = Button(
            text='<' + to_arabic_number(10), font_name='F:/My FONTS/Amiri.ttf', font_size=30,
            color=(0.1, 0.5, 0.5, 1), background_normal='', background_down='',
            background_color=(0, 0, 0, 0), size_hint=(None, None),
            size=(200, 50), pos_hint={'center_x': 0.1, 'center_y': 0.675}
            )
        
        self.tenup.bind(on_release=self.Tenup)
        self.tendn.bind(on_release=self.Tendn)
        
        self.Speed3.bind(on_release=self.speed3)
        self.layout.add_widget(self.SWB)
        self.layout.add_widget(self.SSB)
        self.layout.add_widget(self.MWB)
        self.layout.add_widget(self.MSB)
        self.layout.add_widget(self.SB)
        self.layout.add_widget(self.ST)
        self.layout.add_widget(self.T)
        
        return self.layout
    
    
if __name__ == '__main__':
    Az().run()
