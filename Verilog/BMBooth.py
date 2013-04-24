'''
Created on 2013-2-28
booth
@author: WuYinghao
'''

class Booth(object):
    '''
    classdocs
    '''
    booth_weith=0
    booth_source_code=[]
    booth_file_name=""

    def __init__(self,weith=10):
        self.booth_weith=weith
        self.booth_file_name="booth"+str(self.booth_weith)+".v"
        self.booth_source_code=[]
        
    
    def createBoothCode(self):
        self.booth_source_code.append("module booth_mul"+str(self.booth_weith)+"(w,q,B,AL,AR,AH);\n")
        self.booth_source_code.append("output ["+str(self.booth_weith)+":0]    w;\n")
        self.booth_source_code.append("output [1:0]    q;\n")
        self.booth_source_code.append("input     AL,AR,AH;\n")
        self.booth_source_code.append("input ["+str(self.booth_weith-1)+":0]    B;\n")
        self.booth_source_code.append("wire X2,A,S;\n")
        self.booth_source_code.append("assign q = ({A,S}==2'b10) ? 2'b01 : 2'b00;  \n")
        self.booth_source_code.append("ben_v benc(.S(S), .A(A), .X2(X2), .M2(AH), .M1(AR), .M0(AL));\n")
        self.booth_source_code.append("\t\tbmx_v bmx1(.PP(w[0]), .X2(X2), .A(A), .S(S), .M1(B[0]), .M0(1'b0));")
        for i in range(1,self.booth_weith+1):
            if(i<self.booth_weith):
                bmx="\t\tbmx_v bmx"+str(i+1)+"(.PP(w["+str(i)+"]), .X2(X2), .A(A), .S(S), .M1(B["+str(i)+"]), .M0(B["+str(i-1)+"]));"
            else:
                bmx="\t\tbmx_v bmx"+str(i+1)+"(.PP(w["+str(i)+"]), .X2(X2), .A(A), .S(S), .M1(B["+str(i-1)+"]), .M0(B["+str(i-1)+"]));"             
            self.booth_source_code.append(bmx)
        self.booth_source_code.append("endmodule\n")
        #print self.booth_source_code
        
        
    def writeCodeToFile(self,file_name):
        print "Write Booth file :" + file_name
        file_object = open(file_name, 'w')
        for i in self.booth_source_code:
            file_object.write(i+"\n")
        file_object.close()
    
    
        