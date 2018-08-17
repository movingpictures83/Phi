import sys
import numpy
import math

eps=1e-15

class PhiPlugin:
   def input(self, filename):
      self.myfile = filename
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)
      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)

      # Samples a 2D list of abundances
      self.logdata = []
      for i in range(self.n):
         self.logdata.append(numpy.ndarray(self.m))

      for i in range(self.m):
            contents = lines[i].split(',')
            for j in range(self.n):
               if (float(contents[j+1]) != 0):
                  self.logdata[j][i] = math.log(abs(float(contents[j+1])))
               else:
                  self.logdata[j][i] = math.log(eps)

   def run(self):
      self.PHI = numpy.zeros([self.n, self.n])
      sums = []
      for i in range(self.n):
         sums.append(0)
         for j in range(self.n):
            self.PHI[i][j] = 1 - numpy.var(self.logdata[i] - self.logdata[j]) / numpy.var(self.logdata[i]) 
            if (self.PHI[i][j] <= 0.95):
               self.PHI[i][j] = 0

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write(self.firstline)
            
      for i in range(self.n):
         filestuff2.write(self.bacteria[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.PHI[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



