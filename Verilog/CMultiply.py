'''
Created on 2013-3-15

@author: Administrator
'''

import os
from Verilog.BMBooth import *
from Verilog.BMCompress import *
from Verilog.CBMTest import *


class CMultiply:
    '''
    classdocs
    '''
    all_code=[]
    w_and_q=[]
    w_and_q_weith=[]
    comp_list=[]
    file_name=""
    compress_file_name=""
    booth_file_name=""
    test_file_name=""
    total=0
    minMove=0

    def __init__(self,fileName="D:\multiply\\",compressFileName="D:\multiply\\compress\\",boothFileName="D:\multiply\\booth\\"):
        '''
        Constructor
        '''
        self.all_code=[]
        self.w_and_q=[]
        self.w_and_q_weith=[]
        self.comp_list=[]
        self.file_name=fileName
        self.test_file_name=fileName
        self.compress_file_name=compressFileName
        self.booth_file_name=boothFileName;
        self.total=0
        self.minMove=0
    
    
    def writeToFile(self):
        print "Write multiply file :" + self.file_name
        file_object = open(self.file_name, 'w')
        for i in range(0,len(self.all_code)):
            if(i==0 or i==len(self.all_code)-1):
                file_object.write(self.all_code[i]+"\n")
            else:
                file_object.write("\t"+self.all_code[i]+"\n")
        file_object.close()
    
    
    
    def displayCode(self):
        file_object = open('d:\\thefile.txt', 'w')
        for i in range(0,len(self.all_code)):
            if(i==0 or i==len(self.all_code)-1):
                print self.all_code[i]
                file_object.write(self.all_code[i]+"\r\n")
            else:
                print "\t"+self.all_code[i]
                file_object.write("\t"+self.all_code[i]+"\r\n")
        file_object.close( )


    
    def makeMultiply(self,a,b):
        
        print "######################### Building  " +str(a)+ " X " +str(b)+ "  #########################"

        self.total=a+b-1
        path=self.file_name+"mul_"+str(a)+"x"+str(b)
        try:  
            os.makedirs(path)  
        except Exception:  
            pass
        
        try:
            os.mkdir(self.booth_file_name)
        except Exception:
            pass
        
        try:
            os.mkdir(self.compress_file_name)
        except Exception:
            pass
        
        
        p=Booth(a)
        p.createBoothCode()
        p.writeCodeToFile(self.booth_file_name+"\\booth_mul"+str(a)+".v")
        
        
        self.file_name=path+"\\mul_"+str(a)+"x"+str(b)+".v"
        self.__makeHead(a,b)
        self.__makeInputOutput(a,b)
        wnum=self.__makeWandQ(a,b)
        self.__makeBooth(a,b,wnum)
        
        x_move=[]
        deep=1
        self.__calcCompress(self.w_and_q,self.w_and_q_weith,x_move,deep)
        self.__makeCompress()
        
        self.all_code.append("assign out1 = "+self.comp_list[-1]['output1']+"["+str(self.total)+":0];")
        self.all_code.append("assign out2 = "+self.comp_list[-1]['output2']+"["+str(self.total)+":0];")
        self.__makeEnd()
        
        self.writeToFile()
        print "+++++++++++++++++Multiply Created++++++++++++++++++"
        test=CTest()
        test.createTest(a,b,path)
        print "+++++++++++++++++Test Created++++++++++++++++++"
        print "######################### Built  " +str(a)+ " X " +str(b)+ "  #########################"
        print ""
        print ""

    def __moveCount(self,total_len,input_len,input_move):
        return total_len-(input_len+input_move)


    def __makeEnd(self):
        self.all_code.append("")
        self.all_code.append("")
        self.all_code.append("endmodule")
        self.all_code.append("")
        self.all_code.append("")

    
    
    def __minMove(self,a,b,c,d=1000):
        x=a
        for xx in a,b,c,d:
            if(xx<x):
                x=xx
        return x

    def __maxInputLen(self,compArray):
        print "++++++++++++++++++++++++++++++++++++++"
        print compArray["input1"]
        print compArray["input2"]
        print compArray["input3"]
        if(compArray['type']==42):
            print compArray["input4"]
        print compArray["output_len"]
        print compArray["input_len"]
        print "++++++++++++++++++++++++++++++++++++++"
        
        if(compArray['type']==42):
            self.minMove=self.__minMove(compArray["input1"][2],compArray["input2"][2],compArray["input3"][2],compArray["input4"][2])
        else:
            self.minMove=self.__minMove(compArray["input1"][2],compArray["input2"][2],compArray["input3"][2])
        
        #return min


    def __makeCompress(self):
        count=0
        self.minMove=0
        for comp in self.comp_list:
            #self.__maxInputLen(comp)
            print type(self.minMove)
            print type(comp['output_len'])
            self.all_code.append("wire ["+str(comp['output_len'])+":0]     "+comp['output1']+";")
            self.all_code.append( "wire ["+str(comp['output_len'])+":0]     "+comp['output2']+";")
            self.all_code.append( "")
            if(comp['type']==42):
                
                self.all_code.append( "wire ["+str(comp['input_len'])+":0]     "+str(comp['input1'][0])+";")
                self.all_code.append( "wire ["+str(comp['input_len'])+":0]     "+str(comp['input2'][0])+";")
                self.all_code.append( "wire ["+str(comp['input_len'])+":0]     "+str(comp['input3'][0])+";")
                self.all_code.append( "wire ["+str(comp['input_len'])+":0]     "+str(comp['input4'][0])+";")
                self.all_code.append( "")
                
                high=self.__moveCount(comp['input_len'], comp['input1'][3], comp['input1'][2])
                self.__createMove(comp['input1'], high)
                
                    
                high=self.__moveCount(comp['input_len'], comp['input2'][3], comp['input2'][2])
                self.__createMove(comp['input2'], high)
                
                    
                high=self.__moveCount(comp['input_len'], comp['input3'][3], comp['input3'][2])
                self.__createMove(comp['input3'], high)
                
                
                high=self.__moveCount(comp['input_len'], comp['input4'][3], comp['input4'][2])
                self.__createMove(comp['input4'], high)
                    
                self.all_code.append( "")
                self.all_code.append( "cmp_42_"+str(comp['input_len']+1)+" comp"+str(count)+"(.out1("+comp['output1']+"), .out2("+comp['output2']+"), .a("+comp['input1'][0]+"), .b("+comp['input2'][0]+"), .c("+comp['input3'][0]+"), .d("+comp['input4'][0]+"));")
            else:
                
                self.all_code.append( "wire ["+str(comp['input_len'])+":0]     "+comp['input1'][0]+";")
                self.all_code.append( "wire ["+str(comp['input_len'])+":0]     "+comp['input2'][0]+";")
                self.all_code.append( "wire ["+str(comp['input_len'])+":0]     "+comp['input3'][0]+";")
                self.all_code.append( "")
                
                high=self.__moveCount(comp['input_len'], comp['input1'][3], comp['input1'][2])
                self.__createMove(comp['input1'], high)
                
                      
                high=self.__moveCount(comp['input_len'], comp['input2'][3], comp['input2'][2])
                self.__createMove(comp['input2'], high)
                       
                high=self.__moveCount(comp['input_len'], comp['input3'][3], comp['input3'][2])
                self.__createMove(comp['input3'], high)
                
                self.all_code.append( "")
                self.all_code.append( "cmp_32_"+str(comp['input_len']+1)+" comp"+str(count)+"(.out1("+comp['output1']+"), .out2("+comp['output2']+"), .a("+comp['input1'][0]+"), .b("+comp['input2'][0]+"), .c("+comp['input3'][0]+"));")
            
            self.all_code.append( "")
            self.all_code.append( "")
            count=count+1
        self.all_code.append("")
        self.all_code.append("")
       
       
    def __createMove(self,compArray,high):
        if(compArray[2] > 0 and high > 0):
            if(high>1):
                #if(compArray[2]-self.minMove > 0):
                self.all_code.append("assign "+str(compArray[0])+" = {{"+str(high)+"{"+compArray[1]+ "["+str(compArray[3])+"]}},"+compArray[1]+ ","+str(compArray[2])+"\'h0};")
                #else:
                #    self.all_code.append("assign "+str(compArray[0])+" = {{"+str(high)+"{"+compArray[1]+ "["+str(compArray[3]-self.minMove)+"]}},"+compArray[1]+ "};")
            else:
                #if(compArray[2]-self.minMove > 0):
                self.all_code.append("assign "+str(compArray[0])+" = {"+compArray[1]+ "["+str(compArray[3])+"],"+compArray[1]+ ","+str(compArray[2])+"\'h0};")
                #else:
                #    self.all_code.append("assign "+str(compArray[0])+" = {{"+str(high)+"{"+compArray[1]+ "["+str(compArray[3]-self.minMove)+"]}},"+compArray[1]+ "};")
        else:
            if(compArray[2]==0):
                if(compArray[1]=="Qi"):
                    self.all_code.append("assign "+str(compArray[0])+" = {"+str(high)+"'h0,"+compArray[1]+ "};")
                else:
                    self.all_code.append("assign "+str(compArray[0])+" = {{"+str(high)+"{"+compArray[1]+ "["+str(compArray[3])+"]}},"+compArray[1]+ "};")
            else:
                self.all_code.append("assign "+str(compArray[0])+" = {"+compArray[1]+ ","+str(compArray[2])+"\'h0};")
                   
                
            
    
    """

    """
    def __makeHead(self,a,b):
        function_head_str="module mul_"+str(a)+"x"+str(b)+"(out1,out2,a,b);"
        self.all_code.append(function_head_str)
        self.all_code.append("")
        self.all_code.append("")
        
        
        """
        """
    def __makeInputOutput(self,a,b):
        weith_a=int(a)
        weith_b=int(b)
        self.all_code.append("output ["+str(a+b-1)+":0] out1;")
        self.all_code.append("output ["+str(a+b-1)+":0] out2;")
        self.all_code.append("input["+str(weith_a-1)+":0]    a;")
        self.all_code.append("input["+str(weith_b-1)+":0]    b;")
        self.all_code.append("")
        self.all_code.append("")
        
    
    """
    """
    def __makeWandQ(self,a,b):
        weith_a=int(a)
        weith_b=int(b)
        self.w_and_q=[]
        self.w_and_q_weith=[]
        if(weith_b%2==0):
            w_num=weith_b/2
            self.all_code.append("wire ["+str(weith_b-1)+":0]    Qi;")
            self.w_and_q_weith.append(weith_b-1)
        else:
            w_num=(weith_b+1)/2
            self.all_code.append("wire ["+str(weith_b)+":0]    Qi;")
            self.w_and_q_weith.append(weith_b)
        
        
        self.w_and_q.append("Qi")
        
        for i in range(1,w_num+1):
            self.all_code.append("wire ["+str(weith_a)+":0]    w"+str(i)+";")
            self.w_and_q.append("w"+str(i)+"")
            self.w_and_q_weith.append(weith_a)
     
        self.all_code.append("")
        self.all_code.append("")
        return w_num



    def __makeBooth(self,a,b,wnum):
        self.all_code.append("booth_mul"+str(a)+" booth1(.w(w1),.q(Qi[1:0]),.B(a),.AL(1'b0),.AR(b[0]),.AH(b[1]));") 
        n=1
        m=2
        for i in range(2,wnum+1):
            if(i<wnum):
                self.all_code.append("booth_mul"+str(a)+" booth"+str(i)+"(.w(w"+str(i)+"),.q(Qi["+str(n+2)+":"+str(m)+"]),.B(a),.AL(b["+str(n)+"]),.AR(b["+str(m)+"]),.AH(b["+str(n+2)+"]));")
                n=n+2
                m=m+2
            else:
                if(m>b):
                    self.all_code.append("booth_mul"+str(a)+" booth"+str(i)+"(.w(w"+str(i)+"),.q(Qi["+str(n+2)+":"+str(m)+"]),.B(a),.AL(b["+str(n)+"]),.AR(b["+str(m)+"]),.AH(b["+str(n+2)+"]));")
                else:
                    self.all_code.append("booth_mul"+str(a)+" booth"+str(i)+"(.w(w"+str(i)+"),.q(Qi["+str(n+2)+":"+str(m)+"]),.B(a),.AL(b["+str(n)+"]),.AR(b["+str(m)+"]),.AH(b["+str(b-1)+"]));")
        
        self.all_code.append("")
        self.all_code.append("")   
  
    def __MaxLen(self,a,b):
        m=b[0]
        for i in range(0,len(b)):
            if(m>b[i]):
                m=b[i]
        for i in range(0,len(b)):
            #a[i]=a[i]-m
            b[i]=b[i]-m
        
        max_num=a[0]+b[0]
        for i in range(0,len(a)):
            if(max_num < a[i]+b[i]):
                max_num=a[i]+b[i]
        
        print "A:"+str(a)+ "B:" +str(b)
        print "max:"+str(max_num)
        return max_num,m
  
  
    
  
    def __calcCompress(self,x,x_len,x_move,deep):
        input_num=len(x)
        for i in range(0,len(x_len)):
            if(x_len[i]>self.total):
                x_len[i]=self.total
                #print x_len[i]
        
        
        if(input_num==2):
            return
        
        x_in=[]
        x_next_len_in=[]
        x_next_in=[]
        x_next_move_in=[]
        
        for i in x:
            x_in.append(str(i)+"_in")
        
        comp42_num=input_num/4
        if(input_num%4==3):
            comp32_num=1
            uncomp_num=0
        else:
            if(input_num%4==2 and comp42_num >0):
                comp32_num=2
                uncomp_num=0
                comp42_num=comp42_num-1
            else:
                if(input_num%4==1 and comp42_num >1):
                    comp32_num=3
                    comp42_num=comp42_num-2
                    uncomp_num=0
                else:
                    comp32_num=0
                    uncomp_num=input_num%4
        
        
        for i in range(0,comp42_num):
            comp_42={}
            if(deep==1):
                if(i==0):
                    comp_42['type']=42
                    comp_42['input1']=[x_in[i*4],x[i*4],0,x_len[i*4]]
                    comp_42['input2']=[x_in[i*4+1],x[i*4+1],0,x_len[i*4+1]]
                    comp_42['input3']=[x_in[i*4+2],x[i*4+2],2,x_len[i*4+2]]
                    comp_42['input4']=[x_in[i*4+3],x[i*4+3],4,x_len[i*4+3]]
                    comp_42['input_len']=x_len[i*4+3]+4
                    comp_42['output1']="comp42_"+str(deep)+"_"+str(i)+"_out1"
                    comp_42['output2']="comp42_"+str(deep)+"_"+str(i)+"_out2"
                    comp_42['output_len']=comp_42['input_len']+2
                    x_next_in.append(comp_42['output1'])
                    x_next_in.append(comp_42['output2'])
                    x_next_len_in.append(comp_42['output_len'])
                    x_next_len_in.append(comp_42['output_len'])
                    x_next_move_in.append(0)
                    x_next_move_in.append(1)
                else:
                    comp_42['type']=42
                    comp_42['input1']=[x_in[i*4],x[i*4],0,x_len[i*4]]
                    comp_42['input2']=[x_in[i*4+1],x[i*4+1],2,x_len[i*4+1]]
                    comp_42['input3']=[x_in[i*4+2],x[i*4+2],4,x_len[i*4+2]]
                    comp_42['input4']=[x_in[i*4+3],x[i*4+3],6,x_len[i*4+3]]
                    comp_42['input_len']=x_len[i*4+3]+6
                    comp_42['output1']="comp42_"+str(deep)+"_"+str(i)+"_out1"
                    comp_42['output2']="comp42_"+str(deep)+"_"+str(i)+"_out2"
                    comp_42['output_len']=comp_42['input_len']+2
                    x_next_in.append(comp_42['output1'])
                    x_next_in.append(comp_42['output2'])
                    x_next_len_in.append(comp_42['output_len'])
                    x_next_len_in.append(comp_42['output_len'])
                    x_next_move_in.append(i*4*2-2)
                    x_next_move_in.append(i*4*2-1)
                
            else:
                comp_42['type']=42
                comp_42['input_len'],m=self.__MaxLen(x_len[i*4:i*4+4],x_move[i*4:i*4+4])
                comp_42['input1']=[x_in[i*4],x[i*4],x_move[i*4]-m,x_len[i*4]]
                comp_42['input2']=[x_in[i*4+1],x[i*4+1],x_move[i*4+1]-m,x_len[i*4+1]]
                comp_42['input3']=[x_in[i*4+2],x[i*4+2],x_move[i*4+2]-m,x_len[i*4+2]]
                comp_42['input4']=[x_in[i*4+3],x[i*4+3],x_move[i*4+3]-m,x_len[i*4+3]]
                
                
                print x_len[i*4:i*4+4]
                print x_move[i*4:i*4+4]
                comp_42['output1']="comp42_"+str(deep)+"_"+str(i)+"_out1"
                comp_42['output2']="comp42_"+str(deep)+"_"+str(i)+"_out2"
                comp_42['output_len']=comp_42['input_len']+2
                x_next_in.append(comp_42['output1'])
                x_next_in.append(comp_42['output2'])
                x_next_len_in.append(comp_42['output_len'])
                x_next_len_in.append(comp_42['output_len'])
                x_next_move_in.append(x_move[i*4])
                x_next_move_in.append(x_move[i*4]+1)
            self.comp_list.append(comp_42)
            compress=Compress(comp_42['input_len'],42)
            compress.writeCodeToFile(self.compress_file_name+"\\cmp_42_"+str(comp_42['input_len']+1)+".v")
        
        
        for i in range(0,comp32_num):
            comp_32={}
            if(deep==1):
                if(comp42_num==0 and i==0):
                    comp_32['type']=32
                    comp_32['input1']=[x_in[(comp32_num-i)*(-3)],x[(comp32_num-i)*(-3)],0,x_len[(comp32_num-i)*(-3)]]
                    comp_32['input2']=[x_in[(comp32_num-i)*(-3)+1],x[(comp32_num-i)*(-3)+1],0,x_len[(comp32_num-i)*(-3)+1]]
                    comp_32['input3']=[x_in[(comp32_num-i)*(-3)+2],x[(comp32_num-i)*(-3)+2],2,x_len[(comp32_num-i)*(-3)+2]]
                    comp_32['input_len']=x_len[(comp32_num-i)*(-3)+2]+2
                    comp_32['output1']="comp32_"+str(deep)+"_"+str(i)+"_out1"
                    comp_32['output2']="comp32_"+str(deep)+"_"+str(i)+"_out2"
                    comp_32['output_len']=comp_32['input_len']
                    x_next_in.append(comp_32['output1'])
                    x_next_in.append(comp_32['output2'])
                    x_next_len_in.append(comp_32['output_len'])
                    x_next_len_in.append(comp_32['output_len'])
                    x_next_move_in.append(0)
                    x_next_move_in.append(1)
                else:
                    comp_32['type']=32
                    comp_32['input1']=[x_in[(comp32_num-i)*(-3)],x[(comp32_num-i)*(-3)],0,x_len[(comp32_num-i)*(-3)]]
                    comp_32['input2']=[x_in[(comp32_num-i)*(-3)+1],x[(comp32_num-i)*(-3)+1],2,x_len[(comp32_num-i)*(-3)+1]]
                    comp_32['input3']=[x_in[(comp32_num-i)*(-3)+2],x[(comp32_num-i)*(-3)+2],4,x_len[(comp32_num-i)*(-3)+2]]
                    comp_32['input_len']=x_len[(comp32_num-i)*(-3)+2]+4
                    comp_32['output1']="comp32_"+str(deep)+"_"+str(i)+"_out1"
                    comp_32['output2']="comp32_"+str(deep)+"_"+str(i)+"_out2"
                    comp_32['output_len']=comp_32['input_len']
                    x_next_in.append(comp_32['output1'])
                    x_next_in.append(comp_32['output2'])
                    x_next_len_in.append(comp_32['output_len'])
                    x_next_len_in.append(comp_32['output_len'])
                    x_next_move_in.append((len(x_in)+(comp32_num-i)*(-3))*2-2)
                    x_next_move_in.append((len(x_in)+(comp32_num-i)*(-3))*2-1)              
            else:
                comp_32['type']=32
                print (comp32_num-i)*(-3) 
                print (comp32_num-i)*(-3)+3
                print x_len[(comp32_num-i)*(-3):(comp32_num-i)*(-3)+3]
                if((comp32_num-i)*(-3)+3 < 0):
                    comp_32['input_len'],m=self.__MaxLen(x_len[(comp32_num-i)*(-3):(comp32_num-i)*(-3)+3],x_move[(comp32_num-i)*(-3):(comp32_num-i)*(-3)+3])
                    #for k in range((comp32_num-i)*(-3),(comp32_num-i)*(-3)+3):
                    #    x_len[k]=x_len[k]-m
                    #    x_move[k]=x_move[k]-m
                else:
                    comp_32['input_len'],m=self.__MaxLen(x_len[(comp32_num-i)*(-3):],x_move[(comp32_num-i)*(-3):])
                    #x_len[-3]=x_len[-3]-m
                    #x_move[-3]=x_move[-3]-m
                    #x_len[-2]=x_len[-2]-m
                    #x_move[-2]=x_move[-2]-m
                    #x_len[-1]=x_len[-1]-m
                    #x_move[-1]=x_move[-1]-m
                comp_32['input1']=[x_in[(comp32_num-i)*(-3)],x[(comp32_num-i)*(-3)],x_move[(comp32_num-i)*(-3)]-m,x_len[(comp32_num-i)*(-3)]]
                comp_32['input2']=[x_in[(comp32_num-i)*(-3)+1],x[(comp32_num-i)*(-3)+1],x_move[(comp32_num-i)*(-3)+1]-m,x_len[(comp32_num-i)*(-3)+1]]
                comp_32['input3']=[x_in[(comp32_num-i)*(-3)+2],x[(comp32_num-i)*(-3)+2],x_move[(comp32_num-i)*(-3)+2]-m,x_len[(comp32_num-i)*(-3)+2]]
                
                print x_len[(comp32_num-i)*(-3):]
                print x_move[(comp32_num-i)*(-3):]
                comp_32['output1']="comp32_"+str(deep)+"_"+str(i)+"_out1"
                comp_32['output2']="comp32_"+str(deep)+"_"+str(i)+"_out2"
                comp_32['output_len']=comp_32['input_len']
                x_next_in.append(comp_32['output1'])
                x_next_in.append(comp_32['output2'])
                x_next_len_in.append(comp_32['output_len'])
                x_next_len_in.append(comp_32['output_len'])
                x_next_move_in.append(x_move[(comp32_num-i)*(-3)])
                x_next_move_in.append(x_move[(comp32_num-i)*(-3)]+1)
            self.comp_list.append(comp_32)
            compress=Compress(comp_32['input_len'],32)
            compress.writeCodeToFile(self.compress_file_name+"\\cmp_32_"+str(comp_32['input_len']+1)+".v")
            
                   
        if(uncomp_num==1):
            if(deep==1):
                x_next_in.append(x[-1])  
                x_next_len_in.append(x_len[-1])
                x_next_move_in.append(6)
            else:
                pass

        deep=deep+1
        self.__calcCompress(x_next_in,x_next_len_in,x_next_move_in,deep)
        return
    
  
    
  
  
  
    