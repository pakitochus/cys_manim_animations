#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 08:46:11 2020

@author: pakitochus
"""

from manimlib.imports import *


t_offset = 0
rate = 0.1
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
        # eq4=TextMobject('$A_{\\omega_1}=|H(j\\omega_1)|$')
        # eq4.shift(2*DOWN)
        # eq5=TextMobject('$\\phi_{\\omega_1}=\\angle H(j\\omega_1)$')
        # eq5.shift(3*DOWN)
        
        eq2_2=TextMobject("$\sin(\\omega_2 t)$")
        eq2_2.shift(2*UP).shift(LEFT*FRAME_WIDTH/4)
        eq3_2=TextMobject('$A_{\\omega_2}sin(\\omega_2 t + \\phi_{\\omega_2})$')
        eq3_2.shift(2*UP).shift(RIGHT*(FRAME_WIDTH/4+0.5))
        # eq4_2=TextMobject('$A_{\\omega_2}=|H(j\\omega_2)|$')
        # eq4_2.shift(2*DOWN)
        # eq5_2=TextMobject('$\\phi_{\\omega_2}=\\angle H(j\\omega_2)$')
        # eq5_2.shift(3*DOWN)
        
        c = get_sin(a_out, w, shift=RIGHT)
        c.add_updater(update_curve)
        c2 = get_sin(1, w, shift=LEFT)
        c2.add_updater(update_curve2)
        
        self.play(ShowCreation(square),Write(eq1))
        self.play(ShowCreation(c2))
        self.play(Write(eq2))
        rate=rate/2
        self.play(ShowCreation(c))
        self.play(Write(eq3))
        self.wait(2)
        # self.play(Write(eq4),Write(eq5))
        # self.wait(3)
        
        # Transform equations
        self.play(ReplacementTransform(eq2, eq2_2), ReplacementTransform(eq3, eq3_2))#,
                  # ReplacementTransform(eq4, eq4_2), ReplacementTransform(eq5, eq5_2))
        # self.wait(1)
        w = w*2
        a_out = 0.7
        self.wait(3)
        
        # Transform equations
        eq2_3=TextMobject("$\sin(\\omega_3 t)$")
        eq2_3.shift(2*UP).shift(LEFT*FRAME_WIDTH/4)
        eq3_3=TextMobject('$A_{\\omega_3}sin(\\omega_3 t + \\phi_{\\omega_3})$')
        eq3_3.shift(2*UP).shift(RIGHT*(FRAME_WIDTH/4+0.5))
        # eq4_3=TextMobject('$A_{\\omega_3}=|H(j\\omega_3)|$')
        # eq4_3.shift(2*DOWN)
        # eq5_3=TextMobject('$\\phi_{\\omega_3}=\\angle H(j\\omega_3)$')
        # eq5_3.shift(3*DOWN)
        self.play(ReplacementTransform(eq2_2, eq2_3), ReplacementTransform(eq3_2, eq3_3))#,
                  # ReplacementTransform(eq4_2, eq4_3), ReplacementTransform(eq5_2, eq5_3))
        # self.wait(0.5)
        w = w*1.5
        a_out = 0.3
        self.wait(1)

        # Transform equations
        eq2_4=TextMobject("$\sin(\\omega_4 t)$")
        eq2_4.shift(2*UP).shift(LEFT*FRAME_WIDTH/4)
        eq3_4=TextMobject('$A_{\\omega_4}sin(\\omega_4 t + \\phi_{\\omega_4})$')
        eq3_4.shift(2*UP).shift(RIGHT*(FRAME_WIDTH/4+0.5))
        # eq4_4=TextMobject('$A_{\\omega_4}=|H(j\\omega_4)|$')
        # eq4_4.shift(2*DOWN)
        # eq5_4=TextMobject('$\\phi_{\\omega_4}=\\angle H(j\\omega_4)$')
        # eq5_4.shift(3*DOWN)
        self.play(ReplacementTransform(eq2_3, eq2_4), ReplacementTransform(eq3_3, eq3_4))#,
                  # ReplacementTransform(eq4_3, eq4_4), ReplacementTransform(eq5_3, eq5_4))
        # self.wait(0.5)
        w = w*2
        a_out = 0.05
        self.wait(2)
        
        # Transform equations
        # self.play(ReplacementTransform(eq2_4, eq2_2), ReplacementTransform(eq3_4, eq3_2),
        #           ReplacementTransform(eq4_4, eq4_2), ReplacementTransform(eq5_4, eq5_2))
        # self.wait(0.5)
        # w = w/(2*1.5)
        # a_out = 0.7
        for i in range(10):
            self.wait(0.1)
            rate=rate*1/(i+1)
        
        
        text = TexMobject("y(t)", "=", "A_{\\omega_i}", "\\sin","(", "\\omega_i","t", "+","\\phi_{\\omega_i}",")")
        text.shift(1*DOWN)
        self.remove(c)
        self.remove(c2)
        self.play(ApplyMethod(eq1.shift, 2*UP),
                  ApplyMethod(square.shift, 2*UP))
        self.play(FadeOut(eq2_4), FadeOut(eq3_4), Write(text)) # , FadeOut(eq4_2), FadeOut(eq5_2), 
        
        self.play(ApplyMethod(text[2].set_color, YELLOW))
        self.play(ApplyMethod(text[5].set_color, RED))
        self.play(ApplyMethod(text[8].set_color, GREEN))
        brace_top = Brace(text[2], UP, buff = SMALL_BUFF)
        brace_bottom = Brace(text[8], DOWN, buff = SMALL_BUFF)
        text_top = brace_top.get_text("$|H(j\\omega_i)|$")
        text_top.set_color(YELLOW)
        text_bottom = brace_bottom.get_text("$\\angle H(j\\omega_i)$")
        text_bottom.set_color(GREEN)
        self.play(GrowFromCenter(brace_top),FadeIn(text_top))
        self.wait(2)
        self.play(GrowFromCenter(brace_bottom),FadeIn(text_bottom))
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
    def __init__(self, zeros, polos, u_max=3, v_max=3, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": u_max,
        "v_min": -3,
        "v_max": v_max#,
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
        
    def get_respuesta(self, x):
        hs = x**0 # inicializamos a 1 todo
        if len(self.zeros)>0:
            for el in self.zeros:
                hs = hs*abs(1j*x-el)
        if len(self.polos)>0:
            for el in self.polos:
                hs = hs/abs(1j*x-el)
        return np.array([x*0, x, hs])
        
        
    
    
class SimpleSurface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        z1, z2 = 0,0
        p1=-0.5-0.8660254j
        p2=-0.5+0.8660254j
        surface = TransferFunction((z1,z2),(p1,p2))
        surface_cut = TransferFunction(zeros=(z1,z2),polos=(p1,p2),u_max=0)#, v_max=0)
        self.play(Write(surface))
        N = len(surface)
        self.play(FadeOut(surface[int(N/2):]))
        self.wait(2)
        
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
        cross.set_color(ORANGE)
        wrapper.move_to([p2.real, p2.imag, 0])
        cross2 = Cross(wrapper)
        cross2.set_color(ORANGE)
        
        # Y calculamos las funciones de transferencia
        surface1 = TransferFunction((),())
        surface2 = TransferFunction((),(p1,p2))
        surface3 = TransferFunction((z1,),(p1,p2))
        surface4 = TransferFunction((z1,z2),(p1,p2))
        
        func_graph = ParametricFunction(surface4.get_respuesta,color=GREEN,
                                        t_min = surface4.u_min, t_max=surface4.u_max)
        # graph_lab = axes.get_graph_label(func_graph, label = "|H(j\\omega)|")
        
        # Add text 
        equation=TexMobject("H(s) = \\frac{s^2}{(s^2+s+1)}")
        
        # Set axis labels. 
        omega3d=TexMobject("j\\omega").set_shade_in_3d(True) 
        omega3d.rotate(PI/2,axis=UP).rotate(PI/2,axis=RIGHT).shift(5*UP).shift(0.5*IN)
        sigma3d=TexMobject("\\sigma").set_shade_in_3d(True) 
        sigma3d.rotate(PI,axis=UP).rotate(PI/2,axis=RIGHT).shift(5*RIGHT).shift(0.5*IN)
        self.add(axes,omega3d,sigma3d)
        
        # zero and poles
        zeroes = TexMobject("z_i = 0")
        poles = TexMobject("p_i=-0.5\pm 0.866j")
        
        # Inicio de la animación:
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.play(Write(zero1))
        self.play(Write(zero2))
        self.add_fixed_in_frame_mobjects(zeroes)
        zeroes.to_corner(UR)
        zeroes.set_color(GREEN)
        self.play(Write(zeroes))
        self.wait(2)
        self.play(Write(cross),Write(cross2))
        self.add_fixed_in_frame_mobjects(poles)
        poles.to_corner(UR)
        poles.shift(0.5*DOWN)
        poles.set_color(ORANGE)
        self.play(Write(poles))
        
        
        # group = VGroup(circle, zero1, zero2, cross, cross2)
        
        self.move_camera(phi=70*DEGREES,theta=-45*DEGREES,run_time=3) # phi->elevation, theta->azimuth
        self.play(ApplyMethod(circle.shift, OUT),
                  FadeOut(cross),
                  FadeOut(cross2),
                  FadeOut(zero1),
                  FadeOut(zero2))
        
        # self.wait(2) # innecesario
        # ponemos la ecuación
        self.add_fixed_in_frame_mobjects(equation)
        equation.to_corner(UL)
        self.play(ShowCreation(surface1),Write(equation))
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.wait(1)
        cross.shift(OUT)
        cross2.shift(OUT)
        self.play(FadeIn(cross),
                  FadeIn(cross2))
        self.play(ReplacementTransform(surface1, surface2),
                  ApplyMethod(cross.shift,5*OUT),
                  ApplyMethod(cross2.shift,5*OUT))
        self.wait(2)
        zero1.shift(OUT)
        self.play(FadeIn(zero1))
        self.play(ReplacementTransform(surface2, surface3),
                  ApplyMethod(zero1.shift,IN))
        self.wait(1)
        zero2.shift(OUT)
        self.play(FadeIn(zero2))
        sigma3d.rotate(PI,axis=OUT)
        self.play(ReplacementTransform(surface3, surface4),
                  ApplyMethod(zero2.shift,IN),
                  FadeOut(zeroes),
                  FadeOut(poles))
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.play(ShowCreation(func_graph))
        N= len(surface4)
        self.play(VFadeOut(surface4[int(N/2):]))
        self.move_camera(phi=90*DEGREES,theta=0*DEGREES,run_time=3, 
                         added_anims=[FadeOut(cross),FadeOut(cross2),
                                      FadeOut(zero1),FadeOut(zero2),
                                      FadeOut(circle),FadeOut(equation)])
        self.play(FadeOut(surface4))
        self.wait(2)
        
class Text3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        text3d=TextMobject("This is a 3D text")

        self.add_fixed_in_frame_mobjects(text3d) #<----- Add this
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(ShowCreation(sphere))
        self.wait(2)
        