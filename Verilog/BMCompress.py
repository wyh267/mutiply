'''
Created on 2013-3-15

@author: Administrator
'''

class Compress(object):
    '''
    classdocs
    '''
    compress_num=0
    code_list=[]
    compress_type=0
    
    def __init__(self,num,types):
        '''
        Constructor
        '''
        self.compress_num=num
        self.code_list=[]
        self.compress_type=types
        
        
    
    def createCompress(self):
        if(self.compress_type==42):
            self.code_list.append("module cmp_42_"+str(self.compress_num+1)+"(out1, out2, a, b, c, d);")
            self.compress_num=self.compress_num+1
            self.code_list.append("output ["+str(self.compress_num+1)+":0] out1;")
            self.code_list.append("output ["+str(self.compress_num+1)+":0] out2;")
            self.code_list.append("input ["+str(self.compress_num-1)+":0] a;")
            self.code_list.append("input ["+str(self.compress_num-1)+":0] b;")
            self.code_list.append("input ["+str(self.compress_num-1)+":0] c;")
            self.code_list.append("input ["+str(self.compress_num-1)+":0] d;")
            self.code_list.append("wire ["+str(self.compress_num)+":0] e;")
            self.code_list.append("cmp42_v    cmp0( .S(out1[0]), .CO(out2[0]), .ICO(e[0]), .A(a[0]), .B(b[0]), .C(c[0]), .D(d[0]), .ICI(1'b0) );")
            for i in range(1,self.compress_num+1):
                if(i<self.compress_num):
                    self.code_list.append("cmp42_v    cmp"+str(i)+"( .S(out1["+str(i)+"]), .CO(out2["+str(i)+"]), .ICO(e["+str(i)+"]), .A(a["+str(i)+"]), .B(b["+str(i)+"]), .C(c["+str(i)+"]), .D(d["+str(i)+"]), .ICI(e["+str(i-1)+"]) );")
                else:
                    self.code_list.append("cmp42_v    cmp"+str(i)+"( .S(out1["+str(i)+"]), .CO(out2["+str(i)+"]), .ICO(e["+str(i)+"]), .A(a["+str(i-1)+"]), .B(b["+str(i-1)+"]), .C(c["+str(i-1)+"]), .D(d["+str(i-1)+"]), .ICI(e["+str(i-1)+"]) );")
            self.code_list.append("assign out1["+str(self.compress_num+1)+"]=out1["+str(self.compress_num)+"];")
            self.code_list.append("assign out2["+str(self.compress_num+1)+"]=out2["+str(self.compress_num)+"];")
        else:
            self.code_list.append("module cmp_32_"+str(self.compress_num+1)+"(out1, out2, a, b, c);")
            self.compress_num=self.compress_num+1

            self.code_list.append("output ["+str(self.compress_num-1)+":0] out1;")
            self.code_list.append("output ["+str(self.compress_num-1)+":0] out2;")
            self.code_list.append("input ["+str(self.compress_num-1)+":0] a;")
            self.code_list.append("input ["+str(self.compress_num-1)+":0] b;")
            self.code_list.append("input ["+str(self.compress_num-1)+":0] c;")
            for i in range(0,self.compress_num):
                self.code_list.append("cmp32_v    cmp"+str(i)+"(.S(out1["+str(i)+"]), .CO(out2["+str(i)+"]), .A(a["+str(i)+"]), .B(b["+str(i)+"]), .C(c["+str(i)+"]));")
                 
                    
        self.code_list.append("endmodule")  
            
            
            
    def writeCodeToFile(self,file_name):
        print "Write compress file: "+file_name
        self.createCompress()
        file_object = open(file_name, 'w')
        #print file_name
        for i in self.code_list:
            #print i
            file_object.write(i+"\n")
        file_object.close()
            
            
            
            
            
            
            
            
            
        