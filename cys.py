#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 08:46:11 2020

@author: pakitochus
"""

from manimlib.imports import *


t_offset = 0
rate = 0.05
# global w
w = 1
a_out = 1

def get_sin(A, w, shift=RIGHT):
    return FunctionGraph(lambda x: A*np.sin(w*(x - (t_offset + rate)))) \
            .shift(shift*(FRAME_WIDTH/2+1))
            
def update_curve(c, dt):
    global t_offset
    global w
    global a_out
    other_mob = get_sin(a_out, w, RIGHT)
    c.become(other_mob)
    t_offset += rate

def update_curve2(c, dt):
    global t_offset
    global w
    other_mob = get_sin(1, w, LEFT)
    c.become(other_mob)
    t_offset += rate
    
    
class Curve(Scene):
    def construct(self):
        global w
        global a_out
        global rate
        # filtro
        square = Square()
        eq1=TextMobject("$H(s)$")
        
        #ecuaciones
        eq2=TextMobject("$\sin(\\omega_1 t)$")
        eq2.shift(2*UP).shift(LEFT*FRAME_WIDTH/4)
        eq3=TextMobject('$A_{\\omega_1}sin(\\omega_1 t + \\phi_{\\omega_1})$')
        eq3.shift(2*UP).shift(RIGHT*(FRAME_WIDTH/4+0.5))
        eq4=TextMobject('$A_{\\omega_1}=|H(j\\omega_1)|$')
        eq4.shift(2*DOWN)
        eq5=TextMobject('$\\phi_{\\omega_1}=\\angle H(j\\omega_1)$')
        eq5.shift(3*DOWN)
        
        eq2_2=TextMobject("$\sin(\\omega_2 t)$")
        eq2_2.shift(2*UP).shift(LEFT*FRAME_WIDTH/4)
        eq3_2=TextMobject('$A_{\\omega_2}sin(\\omega_2 t + \\phi_{\\omega_2})$')
        eq3_2.shift(2*UP).shift(RIGHT*(FRAME_WIDTH/4+0.5))
        eq4_2=TextMobject('$A_{\\omega_2}=|H(j\\omega_2)|$')
        eq4_2.shift(2*DOWN)
        eq5_2=TextMobject('$\\phi_{\\omega_2}=\\angle H(j\\omega_2)$')
        eq5_2.shift(3*DOWN)
        
        c = get_sin(a_out, w, shift=RIGHT)
        c.add_updater(update_curve)
        c2 = get_sin(1, w, shift=LEFT)
        c2.add_updater(update_curve2)
        
        self.play(ShowCreation(square))
        self.play(Write(eq1))
        self.play(ShowCreation(c2))
        self.play(Write(eq2))
        rate=rate/2
        self.play(ShowCreation(c))
        self.play(Write(eq3))
        self.wait(2)
        self.play(Write(eq4),Write(eq5))
        self.wait(3)
        
        # Transform equations
        self.play(ReplacementTransform(eq2, eq2_2), ReplacementTransform(eq3, eq3_2),
                  ReplacementTransform(eq4, eq4_2), ReplacementTransform(eq5, eq5_2))
        self.wait(1)
        w = w*2
        a_out = 0.7
        self.wait(3)
        
        # Transform equations
        eq2_3=TextMobject("$\sin(\\omega_3 t)$")
        eq2_3.shift(2*UP).shift(LEFT*FRAME_WIDTH/4)
        eq3_3=TextMobject('$A_{\\omega_3}sin(\\omega_3 t + \\phi_{\\omega_3})$')
        eq3_3.shift(2*UP).shift(RIGHT*(FRAME_WIDTH/4+0.5))
        eq4_3=TextMobject('$A_{\\omega_3}=|H(j\\omega_3)|$')
        eq4_3.shift(2*DOWN)
        eq5_3=TextMobject('$\\phi_{\\omega_3}=\\angle H(j\\omega_3)$')
        eq5_3.shift(3*DOWN)
        self.play(ReplacementTransform(eq2_2, eq2_3), ReplacementTransform(eq3_2, eq3_3),
                  ReplacementTransform(eq4_2, eq4_3), ReplacementTransform(eq5_2, eq5_3))
        self.wait(0.5)
        w = w*1.5
        a_out = 0.3
        self.wait(1)

        # Transform equations
        eq2_4=TextMobject("$\sin(\\omega_4 t)$")
        eq2_4.shift(2*UP).shift(LEFT*FRAME_WIDTH/4)
        eq3_4=TextMobject('$A_{\\omega_4}sin(\\omega_4 t + \\phi_{\\omega_4})$')
        eq3_4.shift(2*UP).shift(RIGHT*(FRAME_WIDTH/4+0.5))
        eq4_4=TextMobject('$A_{\\omega_4}=|H(j\\omega_4)|$')
        eq4_4.shift(2*DOWN)
        eq5_4=TextMobject('$\\phi_{\\omega_4}=\\angle H(j\\omega_4)$')
        eq5_4.shift(3*DOWN)
        self.play(ReplacementTransform(eq2_3, eq2_4), ReplacementTransform(eq3_3, eq3_4),
                  ReplacementTransform(eq4_3, eq4_4), ReplacementTransform(eq5_3, eq5_4))
        self.wait(0.5)
        w = w*2
        a_out = 0.05
        self.wait(2)
        
        # Transform equations
        self.play(ReplacementTransform(eq2_4, eq2_2), ReplacementTransform(eq3_4, eq3_2),
                  ReplacementTransform(eq4_4, eq4_2), ReplacementTransform(eq5_4, eq5_2))
        self.wait(0.5)
        w = w/(2*1.5)
        a_out = 0.7
        for i in range(10):
            self.wait(0.1)
            rate=rate*1/(i+1)
        
        # VOY POR AQUI.. 
        text = TexMobject("y(t)", "=", "A_{\\omega_2}", "\\sin","(", "\\omega_2","t", "+","\\phi_{\\omega_2}",")")
        text.shift(1*DOWN)
        self.remove(c)
        self.remove(c2)
        self.play(ApplyMethod(eq1.shift, 2*UP),
                  ApplyMethod(square.shift, 2*UP))
        self.play(FadeOut(eq2_2), FadeOut(eq3_2), FadeOut(eq4_2), 
                  FadeOut(eq5_2), Write(text))
        
        self.play(ApplyMethod(text[2].set_color, YELLOW))
        self.play(ApplyMethod(text[5].set_color, RED))
        self.play(ApplyMethod(text[8].set_color, GREEN))
        brace_top = Brace(text[2], UP, buff = SMALL_BUFF)
        brace_bottom = Brace(text[8], DOWN, buff = SMALL_BUFF)
        text_top = brace_top.get_text("$|H(j\\omega)|$")
        text_bottom = brace_bottom.get_text("$\\angle H(j\\omega)$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
            )
        self.wait(2)
        # self.play(ApplyMethod(eq6.set_color_by_tex, "A", RED, substring=True))
        # eq6.set_color_by_tex(tex, color)
        self.wait(5)


class Text(Scene): 
    def construct(self):
        text = TexMobject("y(t)", "=", "A_{\\omega_2}", "\\sin","(", "\\omega_2","t", "+","\\phi_{\\omega_2}",")")
        text.shift(2.5*DOWN)
        self.add(text)
        self.play(ApplyMethod(text[2].set_color, YELLOW))
        self.play(ApplyMethod(text[5].set_color, RED))
        self.play(ApplyMethod(text[8].set_color, GREEN))
        brace_top = Brace(text[2], UP, buff = SMALL_BUFF)
        brace_bottom = Brace(text[8], DOWN, buff = SMALL_BUFF)
        text_top = brace_top.get_text("$|H(j\\omega)|$")
        text_bottom = brace_bottom.get_text("$\\angle H(j\\omega)$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
            )
        self.wait(2)
        
        
class TransferFunction(ParametricSurface):
    """
    Wrapper para pintar en 3D una función de transferencia H(s)
    Hay que pasarle zeros y polos, las posiciones de cad uno de ellos. 
    Pueden ser tuplas, listas o arrays. 
    """
    def __init__(self, zeros, polos, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": 3,
        "v_min": -3,
        "v_max": 3#,
        # "checkerboard_colors": []
        }
        self.zeros=zeros
        self.polos=polos
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        s = x+1j*y # s es el plano complejo sigma + jomega
        z = s**0 # inicializamos a 1 todo el plano
        if len(self.zeros)>0:
            for el in self.zeros:
                z = z*(s-el)
        if len(self.polos)>0:
            for el in self.polos:
                z = z/(s-el)
        return np.array([x,y,abs(z)])
    
        
class ZeroPoles(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # Pintamos el círculo w0
        circle=Circle()
        circle.set_color(RED)
        
        # Establecemos los polos y ceros. 
        z1, z2 = 0,0
        p1=-0.5-0.8660254j
        p2=-0.5+0.8660254j
        
        # Pintamos los ceros
        zero1 = Circle()
        zero1.scale(0.1).set_color(GREEN)
        zero2 = Circle()
        zero2.scale(0.2).set_color(GREEN)
        
        # Y los polos, para lo cual usamos un wrapper que no se mostrará
        wrapper = Square(side_length=0.25)
        wrapper.move_to([p1.real, p1.imag, 0])
        cross = Cross(wrapper)
        cross.set_color(BLUE)
        wrapper.move_to([p2.real, p2.imag, 0])
        cross2 = Cross(wrapper)
        cross2.set_color(BLUE)
        
        # Y calculamos las funciones de transferencia
        surface1 = TransferFunction((),())
        surface2 = TransferFunction((),(p1,p2))
        surface3 = TransferFunction((z1,),(p1,p2))
        surface4 = TransferFunction((z1,z2),(p1,p2))
        
        # Inicio de la animación:
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.play(Write(zero1))
        self.play(Write(zero2))
        self.wait(2)
        self.play(Write(cross),Write(cross2))
        
        group = VGroup(circle, zero1, zero2, cross, cross2)
        
        self.move_camera(phi=70*DEGREES,theta=-45*DEGREES,run_time=3) # phi->elevation, theta->azimuth
        self.play(ApplyMethod(group.shift, OUT))
        
        self.wait(2)
        self.play(Write(surface1))
        # self.begin_ambient_camera_rotation(rate=0.1) 
        self.wait(2)
        self.play(ReplacementTransform(surface1, surface2))
        self.wait(0.5)
        self.play(ReplacementTransform(surface2, surface3))
        self.wait(0.5)
        self.play(ReplacementTransform(surface3, surface4))
        self.wait(0.5)
        # self.stop_ambient_camera_rotation()