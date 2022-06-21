import pygame
from random import uniform
import math
import sys

class Vectorization():
    def __init__(self):
        self.origin = [0,0]
        self.i = [1,0]
        self.j = [0,1]
    
    def vector(self, xp, yp):
        return [xp, yp]
    
    def diference(self, p1, p2):
        d = [p1[0]-p2[0], p1[1] - p2[1]]
        return d

    def sum(self, p1, p2):
        s = [p1[0]+p2[0], p1[1] + p2[1]]
        return s

    def module(self, p):
        module_p = (p[0]**2 + p[1]**2)**(1/2)
        return module_p
    
    def in_product(self, p1, p2):
        p = p1[0]*p2[0] +  p2[1]*p1[1]
        return p
    
    def projectation(self, origin, cord: str):
        if cord == 'x':
            origin_base_x = self.in_product(self.i, origin)*self.i[0]
            origin_base_y = self.in_product(self.i, origin)*self.i[1]
            return [origin_base_x, origin_base_y]
        if cord == 'y':
            origin_base_x = self.in_product(self.j, origin)*self.j[0]
            origin_base_y = self.in_product(self.j, origin)*self.j[1]
            return [origin_base_x, origin_base_y]

class GameStage():
    def __init__(self):
        self.stage = 'intro'
    
    def intro(self):
        screen.fill((0,0,0))
        x_button, y_button = x_welc + text_welcome.get_width()/2 - button_blue.get_width()/2, y_welc + text_welcome.get_height() + 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit() 
                
                if event.key == pygame.K_RETURN:
                    self.stage = 'stage1'
                if event.key == pygame.K_LEFT:
                    self.stage = 'intro'
                if event.key == pygame.K_RIGHT:
                    self.stage = 'stage1'
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x_button <= x <= x_button + button_blue.get_width() and y_button <= y <= y_button + button_blue.get_height():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1 and x_button <= x <= x_button + button_blue.get_width() and y_button <= y <= y_button + button_blue.get_height():
                    self.stage = 'stage1'
        
        screen.blit(text_welcome, (x_welc, y_welc))
        screen.blit(button_blue, (x_button, y_button)) 
        screen.blit(text_button_intro, (x_button + button_blue.get_width()/2 - text_button_intro.get_width()/2, y_button + button_blue.get_height()/2 - text_button_intro.get_height()/2))   

        pygame.display.flip()
    
    def stage1(self):
        screen.fill((0,0,0))
        x_button, y_button = xb + button_blue.get_width()/2, yb + barra.get_height() + 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    self.stage = 'stage2' 
                if event.key == pygame.K_LEFT:
                    self.stage = 'intro'
                if event.key == pygame.K_RIGHT:
                    self.stage = 'stage2'
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x_button <= x <= x_button + button_blue.get_width() and y_button <= y <= y_button + button_blue.get_height():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1 and x_button <= x <= x_button + button_blue.get_width() and y_button <= y <= y_button + button_blue.get_height():
                    self.stage = 'stage2'
                
        #preenchimento das cargas
        screen.blit(barra, (xb, yb))
        for positions in position_p1.values():
            screen.blit(proton, (positions[0], positions[1]))
        for positions in position_e1.values():
            screen.blit(eletron, (positions[0], positions[1]))
        screen.blit(text_stage1, (width/2 - text_stage1.get_width()/2, 15))
        screen.blit(button_blue, (x_button, y_button))
        screen.blit(text_proton, (width - text_proton.get_width() - 5, 5))
        screen.blit(text_button_stage2, (x_button + button_blue.get_width()/2 - text_button_stage2.get_width()/2, y_button + button_blue.get_height()/2 - text_button_stage2.get_height()/2))
        screen.blit(text_eletron, (width - text_proton.get_width() - 5, 5 + text_proton.get_height() + 5))
            
        pygame.display.flip()
    
    def stage2(self):
        screen.fill((0,0,0))
        gaussiana = False
        for particula in position_e1f.keys():
            if particula == '0':
                if position_e1f[particula][0] <= x_min:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + barra.get_height()/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '1':
                if position_e1f[particula][0] >= x_max:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + barra.get_height()/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '2':
                if position_e1f[particula][0] <= x_min:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + (2*barra.get_height())/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '3':
                if position_e1f[particula][0] >= x_max:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + (2*barra.get_height())/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '4':
                if position_e1f[particula][0] <= x_min:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + (3*barra.get_height())/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '5':
                if position_e1f[particula][0] >= x_max:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + (3*barra.get_height())/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    self.stage = 'stage3'
                if event.key == pygame.K_LEFT:
                    self.stage = 'stage1'
                if event.key == pygame.K_RIGHT:
                    self.stage = 'stage3'
                if event.key == pygame.K_g:
                    if gaussiana == False:
                        gaussiana = True
                    else:
                        gaussiana = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if  x_button2 <= x <= x_button2 + button_blue.get_width() and y_button2 <= y <= y_button2 + button_blue.get_height() or x_button3 <= x <= x_button3 + button_blue.get_width() and y_button3 <= y <= y_button3 + button_blue.get_height() or x_button <= x <= x_button + button_blue.get_width() and y_button <= y <= y_button + button_blue.get_height():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1 and x_button3 <= x <= x_button3 + button_blue.get_width() and y_button3 <= y <= y_button3 + button_blue.get_height():
                    for positions in position_e1f.values():
                        positions[2] = [False, False, False, False]
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1 and x_button2 <= x <= x_button2 + button_blue.get_width() and y_button2 <= y <= y_button2 + button_blue.get_height():
                    for positions in position_e1f.values():
                        for i in positions[2]:
                            i = False
                    for positions in position_e1f.values():
                        positions[0] = uniform(x_min, x_max)
                        positions[1] = uniform(y_min, y_max)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1 and x_button <= x <= x_button + button_blue.get_width() and y_button <= y <= y_button + button_blue.get_height():
                    for particula in position_e1f.keys():
                        if particula == '0':
                            if position_e1f[particula][0] >= x_min:
                                position_e1f[particula][2][0] = True
                            if position_e1f[particula][1] >= yb + barra.get_height()/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + barra.get_height()/4:
                                position_e1f[particula][2][2] = True
                        if particula == '1':
                            if position_e1f[particula][0] <= x_max:
                                position_e1f[particula][2][1] = True
                            if position_e1f[particula][1] >= yb + barra.get_height()/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + barra.get_height()/4:
                                position_e1f[particula][2][2] = True
                        if particula == '2':
                            if position_e1f[particula][0] >= x_min:
                                position_e1f[particula][2][0] = True
                            if position_e1f[particula][1] >= yb + (2*barra.get_height())/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + (2*barra.get_height())/4:
                                position_e1f[particula][2][2] = True
                        if particula == '3':
                            if position_e1f[particula][0] <= x_max:
                                position_e1f[particula][2][1] = True
                            if position_e1f[particula][1] >= yb + (2*barra.get_height())/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + (2*barra.get_height())/4:
                                position_e1f[particula][2][2] = True
                        if particula == '4':
                            if position_e1f[particula][0] >= x_min:
                                position_e1f[particula][2][0] = True
                            if position_e1f[particula][1] >= yb + (3*barra.get_height())/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + (3*barra.get_height())/4:
                                position_e1f[particula][2][2] = True
                        if particula == '5':
                            if position_e1f[particula][0] <= x_max:
                                position_e1f[particula][2][1] = True
                            if position_e1f[particula][1] >= yb + (3*barra.get_height())/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + (3*barra.get_height())/4:
                                position_e1f[particula][2][2] = True
                                       
        #preenchimento das cargas
        for positions in position_e1f.values():
            if positions[2][0]:
                positions[0] -= 1
            if positions[2][1]:
                positions[0] += 1
            if positions[2][2]:
                positions[1] += 1
            if positions[2][3]:
                positions[1] -= 1

        screen.blit(barra, (xb, yb))
        for positions in position_e1f.values():
            screen.blit(eletron, (positions[0], positions[1]))
            screen.blit(text_proton, (width - text_proton.get_width() - 5, 5))
        screen.blit(button_blue, (x_button3, y_button3))
        screen.blit(text_button_pause, (x_button3 + button_blue.get_width()/2 - text_button_pause.get_width()/2, y_button3 + button_blue.get_height()/2 - text_button_pause.get_height()/2))
        screen.blit(text_eletron, (width - text_proton.get_width() - 5, 5 + text_proton.get_height() + 5))
        screen.blit(button_blue, (x_button, y_button))
        screen.blit(button_blue, (x_button2, y_button2))
        screen.blit(text_button_restart, (x_button2 + button_blue.get_width()/2 - text_button_restart.get_width()/2, y_button2 + button_blue.get_height()/2 - text_button_restart.get_height()/2))
        screen.blit(text_button_stage2, (x_button + button_blue.get_width()/2 - text_button_stage2.get_width()/2, y_button + button_blue.get_height()/2 - text_button_stage2.get_height()/2))

        #pygame.draw.circle(screen, (128,128,128), (xp, yp), barra.get_width()/3, width=2)


        pygame.display.flip()
    
    def stage3(self):
        screen.fill((0,0,0))

        for particula in position_e1f.keys():
            if particula == '0':
                if position_e1f[particula][0] <= x_min:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + barra.get_height()/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '1':
                if position_e1f[particula][0] >= x_max:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + barra.get_height()/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '2':
                if position_e1f[particula][0] <= x_min:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + (2*barra.get_height())/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '3':
                if position_e1f[particula][0] >= x_max:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + (2*barra.get_height())/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '4':
                if position_e1f[particula][0] <= x_min:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + (3*barra.get_height())/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False
            if particula == '5':
                if position_e1f[particula][0] >= x_max:
                    position_e1f[particula][2][0] = False
                    position_e1f[particula][2][1] = False
                if round(position_e1f[particula][1]) == round(yb + (3*barra.get_height())/4):
                    position_e1f[particula][2][3] = False
                    position_e1f[particula][2][2] = False

        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_LEFT:
                    self.stage = 'stage2'
                if event.key == pygame.K_RIGHT:
                    self.stage = 'stage_final'
                if event.key == pygame.K_g:
                    pygame.draw.circle(screen, (139,0,0), (xp, yp), barra.get_width()/3)
                if event.key == pygame.K_r:
                    for positions in position_e1f.values():
                        positions[0] = uniform(x_min, x_max)
                        positions[1] = uniform(y_min, y_max)
                if event.key == pygame.K_2:
                    pass
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if  x_button2 <= x <= x_button2 + button_blue.get_width() and y_button2 <= y <= y_button2 + button_blue.get_height() or x_button3 <= x <= x_button3 + button_blue.get_width() and y_button3 <= y <= y_button3 + button_blue.get_height() or x_button <= x <= x_button + button_blue.get_width() and y_button <= y <= y_button + button_blue.get_height():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1 and x_button3 <= x <= x_button3 + button_blue.get_width() and y_button3 <= y <= y_button3 + button_blue.get_height():
                    for positions in position_e1f.values():
                        positions[2] = [False, False, False, False]
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1 and x_button2 <= x <= x_button2 + button_blue.get_width() and y_button2 <= y <= y_button2 + button_blue.get_height():
                    for positions in position_e1f.values():
                        positions[0] = uniform(x_min, x_max)
                        positions[1] = uniform(y_min, y_max)
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1 and x_button <= x <= x_button + button_blue.get_width() and y_button <= y <= y_button + button_blue.get_height():
                    for particula in position_e1f.keys():
                        if particula == '0':
                            if position_e1f[particula][0] >= x_min:
                                position_e1f[particula][2][0] = True
                            if position_e1f[particula][1] >= yb + barra.get_height()/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + barra.get_height()/4:
                                position_e1f[particula][2][2] = True
                        if particula == '1':
                            if position_e1f[particula][0] <= x_max:
                                position_e1f[particula][2][1] = True
                            if position_e1f[particula][1] >= yb + barra.get_height()/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + barra.get_height()/4:
                                position_e1f[particula][2][2] = True
                        if particula == '2':
                            if position_e1f[particula][0] >= x_min:
                                position_e1f[particula][2][0] = True
                            if position_e1f[particula][1] >= yb + (2*barra.get_height())/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + (2*barra.get_height())/4:
                                position_e1f[particula][2][2] = True
                        if particula == '3':
                            if position_e1f[particula][0] <= x_max:
                                position_e1f[particula][2][1] = True
                            if position_e1f[particula][1] >= yb + (2*barra.get_height())/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + (2*barra.get_height())/4:
                                position_e1f[particula][2][2] = True
                        if particula == '4':
                            if position_e1f[particula][0] >= x_min:
                                position_e1f[particula][2][0] = True
                            if position_e1f[particula][1] >= yb + (3*barra.get_height())/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + (3*barra.get_height())/4:
                                position_e1f[particula][2][2] = True
                        if particula == '5':
                            if position_e1f[particula][0] <= x_max:
                                position_e1f[particula][2][1] = True
                            if position_e1f[particula][1] >= yb + (3*barra.get_height())/4:
                                position_e1f[particula][2][3] = True
                            if position_e1f[particula][1] <= yb + (3*barra.get_height())/4:
                                position_e1f[particula][2][2] = True
        #movimentation
        for positions in position_e1f.values():
            if positions[2][0]:
                positions[0] -= 1
            if positions[2][1]:
                positions[0] += 1
            if positions[2][2]:
                positions[1] += 1
            if positions[2][3]:
                positions[1] -= 1
            
        #diference vector
        for positions in position_e1f.values():
            VectorOperation = Vectorization()
            vector_d = VectorOperation.diference(p1=[xp, yp], p2=[positions[0], positions[1]])
            module_d = VectorOperation.module(vector_d)
            E = eletric_filed(module_d)
            positions[4] = E

            #normalization 
            for i in range(len(vector_d)):
                vector_d[i] = vector_d[i]/module_d
            
            #campo gerado pela carga dada
            if positions[2][0] == True or positions[2][1] == True or positions[2][2] == True or positions[2][3] == True:
                positions[3][0] = xp + E*vector_d[0]
                positions[3][1] = yp + E*vector_d[1]
        #gaussiana



        #eletric result field (soma vetorial)
        result_vectorx = 0
        result_vectory = 0
        for positions in position_e1f.values():
            charge_fild_x = VectorOperation.projectation(positions[3], 'x')
            charge_fiel_y = VectorOperation.projectation(positions[3], 'y')
            result_vectorx += VectorOperation.module(charge_fild_x)
            result_vectory += VectorOperation.module(charge_fiel_y)
            
        
        #fill
        result_vector_text = game_font.render(f'E = {round(result_vectorx)}i + {round(result_vectory)}j V/m', True, (128, 128, 128))
        screen.blit(barra, (xb, yb))
        positions_aux = []
        for positions in position_e1f.values():
            screen.blit(eletron, (positions[0], positions[1]))
            teta = math.atan(positions[1]/positions[0])
            positions_aux.append([positions[0], positions[1], teta, positions[4]])

            #retas que ligam o ponto as cargas
            pygame.draw.polygon(screen, (255,255,255), [(positions[0] + 4, positions[1] + 4), (xp + 4, yp + 4), (xp + 4, yp + 4)], width=0)
        
        #desenho do vetor campo elétrico para cada partícula em relação ao ponto
        positions_aux = sorted(positions_aux, key=lambda position: position[1])
        #l = 5
        #for particula in positions_aux:
            #pygame.draw.polygon(screen, (123,104,238), [(xp, yp), (xp + 10*particula[3]*math.cos(particula[2]), yp - 10*particula[3]*math.sin(particula[2])), (xp + 10*particula[3]*math.cos(particula[2]), yp - 10*particula[3]*math.sin(particula[2]))])

        screen.blit(point, (xp, yp))
        screen.blit(button_blue, (x_button, y_button))
        screen.blit(button_blue, (x_button2, y_button2))
        screen.blit(button_blue, (x_button3, y_button3))
        screen.blit(text_button_pause, (x_button3 + button_blue.get_width()/2 - text_button_pause.get_width()/2, y_button3 + button_blue.get_height()/2 - text_button_pause.get_height()/2))
        screen.blit(text_button_restart, (x_button2 + button_blue.get_width()/2 - text_button_restart.get_width()/2, y_button2 + button_blue.get_height()/2 - text_button_restart.get_height()/2))
        screen.blit(text_button_stage2, (x_button + button_blue.get_width()/2 - text_button_stage2.get_width()/2, y_button + button_blue.get_height()/2 - text_button_stage2.get_height()/2))
        screen.blit(text_point, (xp - text_point.get_width()/2, yp-text_point.get_height()-3))
        screen.blit(text_proton, (width - text_proton.get_width() - 5, 5))
        screen.blit(text_eletron, (width - text_proton.get_width() - 5, 5 + text_proton.get_height() + 5))
        #screen.blit(result_vector_text, (width/2 - result_vector_text.get_width()/2, yb + barra.get_height() + 15))
        pygame.draw.circle(screen, (128,128,128), (xp + point.get_width()/2, yp + point.get_height()/2), barra.get_width()/3, width=2)
        


        pygame.display.flip()
        
    def stage_final(self):
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit() 
                if event.key == pygame.K_LEFT:
                    self.stage = 'stage2'
                if event.key == pygame.K_RIGHT:
                    self.stage = 'stage_final'
        screen.blit(text_autor1, (width/2 - text_autor1.get_width()/2, heigth/2 - text_autor1.get_height()/2 - text_autor2.get_height() - 5))
        screen.blit(text_autor2, (width/2 - text_autor2.get_width()/2, heigth/2 - text_autor2.get_height()/2))
        screen.blit(text_autor3,(width/2 - text_autor3.get_width()/2, text_autor2.get_height()+ 5 + heigth/2 - text_autor3.get_height()/2))
        #screen.blit(einstein, (width/2 - einstein.get_width()/2, heigth/2 - einstein.get_height()/2))
        #screen.blit(text_final, (width/2 - text_final.get_width()/2, heigth/2 + einstein.get_height()/2 + 20))

        pygame.display.flip()
    
    def stage_maneger(self):
        if self.stage == 'intro':
            self.intro()
        if self.stage == 'stage1':
            self.stage1()
        if self.stage == 'stage2':
            self.stage2()
        if self.stage == 'stage_final':
            self.stage_final()
        if self.stage == 'stage3':
            self.stage3()

def position(x_min, y_min, x_max, y_max):
    x = uniform(x_min, x_max)
    y = uniform(y_min, y_max)
    return [x,y]

def eletric_filed(d):
    k = 9*10**(9)
    e = 1.6*10**(-9)
    E = k*e/(d**2)
    return E

def charges_positions():
    pass

pygame.init()

width, heigth = 640, 480

screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Learning Physics')

#objetos
proton = pygame.image.load("proton1.png")
eletron = pygame.image.load("eletron.png")
barra = pygame.image.load("barra.png")
point = pygame.image.load("point.gif")
button_blue = pygame.image.load("button_rect_blue.png")
button_blue_stage3 = pygame.image.load("button_stage3.png")

clock = pygame.time.Clock()

#variaveis
n1_p, n1_e = 4, 4
n2_p, n2_e = 4, 6
excesso = (n1_p - n1_e) - (n2_p - n2_e)

#posicionamento inicial da barra
xb = width/2 - barra.get_width()/2 
yb = heigth/2 - barra.get_height()/2
x_button, y_button = xb - 8, yb + barra.get_height() + 5
x_button2, y_button2 = x_button + button_blue.get_width() + 5, yb + barra.get_height() + 5
x_button3, y_button3 = xb + button_blue.get_width()/2 - 8, yb - button_blue.get_height() - 5

x_min, x_max = xb , xb + barra.get_width() - proton.get_width() 
y_min, y_max = yb , yb + barra.get_height() - proton.get_width()
xp, yp = width/2 - point.get_width()/2, heigth/2 - 100


#preenchimento do display
#screen.fill((0,0,0))
game_font = pygame.font.SysFont("Arial", 20)
text_proton = game_font.render("Blue: próton", True, (0,0,255))
text_eletron = game_font.render("Red: elétron", True, (255,0,0))
text_final = game_font.render("Bons estudos!!", True, (128,128,128))
text_point = game_font.render("P", True, (0,0,0))
text_autor1 = game_font.render("By: © João Victor", True, (128,128,128))
text_button_stage2 = game_font.render("START", True, (0,0,0))
text_button_restart = game_font.render("RESTART", True, (0,0,0))
text_button_intro = game_font.render("Vamos lá!", True, (0,0,0))
text_button_pause = game_font.render("PAUSE", True, (0,0,0))
text_autor2 = game_font.render("GitHub: https://github.com/Nogueira23", True, (128,128,128))
text_autor3 = game_font.render("E-mail: jvictor.n.m23@gmail.com.br", True, (128,128,128))
text_stage2 = game_font.render("As partículas tendem a ficarem diamentralmente opostas", True, (128,128,128))
text_stage1 = game_font.render("Barra antes da transferência de cargas", True, (128,128,128))
text_welcome = game_font.render("Hello, Are You ready to learn about Physics?", True, (128,128,128))
x_welc, y_welc = width/2 - text_welcome.get_width()/2 , heigth/2 - text_welcome.get_height()/2

#posicição inicial para as partículas
position_p1 = {}
position_e1 = {}
for i in range(50):
    positions = position(x_min, y_min, x_max, y_max)
    position_p1[f'{i}'] = positions
for i in range(55):
    positions = position(x_min, y_min, x_max, y_max)
    position_e1[f'{i}'] = positions

#posições finais para as partículas
position_e1f = {}
for i in range(6):
    positions = position(x_min, y_min, x_max, y_max)
    position_e1f[f'{i}'] = positions
    positions.append([False, False, False, False])
    positions.append([xp, yp])
    positions.append(0)

game_stage = GameStage()
while True:
    game_stage.stage_maneger()
    clock.tick(50)