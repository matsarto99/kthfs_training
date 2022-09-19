import numpy as np
import matplotlib.pyplot as plt

class Plot(object):
    def __init__(self,freq=1,dt=0.01):
        # frequency of the base sine wave
        self.freq = freq

        # sampling time
        self.dt = dt 
    

    def _lambda(self,t):
        return 5*np.sin(2*np.pi*self.freq*t)


    def h(self,t):
        return 3*np.pi*np.exp(-1*self._lambda(t))


    def static_plot(self):
        # array of sampling points
        t = np.linspace(0,self.freq,int(360/self.dt))
        plt.plot(t,self.h(t))
        plt.show()


    def dynamic_plot(self, sim_time):
        # sim_time: total simulation time

        loop_length = int(sim_time/self.dt) + 1 

        # lenght of the plotting window
        plt_window = self.freq
        
        fig, ax = plt.subplots(1)

        y = np.array([])

        for i in range(loop_length):
            if i == 0:
                t = np.array([0])
            else:
                t = np.append(t, t[-1] + self.dt)
            y = np.append(y, self.h(t[i]))

            l_wnd = 0 if int(i + 1 - plt_window / self.dt) < 1 else int(i + 1 - plt_window / self.dt)

            ax.clear()
            ax.set_title("Function")
            ax.plot(t[l_wnd:], y[l_wnd:], 'r--')
            ax.legend(["h"])
            ax.set_ylabel("h")

            plt.pause(0.005)
        
        plt.show()





