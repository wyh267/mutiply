'''
Created on 2013-3-19

@author: Administrator
'''

class CTest(object):
    '''
    classdocs
    '''

    test_code=[]
    
    def __init__(self):
        '''
        Constructor
        '''
        self.test_code=[]
        

    def createTest(self,a,b,path):
        """
        self.test_code.append("`timescale 1ns / 1ps                                                               ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("module tb_mul_"+str(a)+"x"+str(b)+";                                                               ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("reg clk;                                                                           ")
        self.test_code.append("reg rst;                                                                           ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("parameter size_a = "+str(a)+";                                                             ")
        self.test_code.append("parameter size_b = "+str(b)+";                                                             ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("initial begin                                                                      ")
        self.test_code.append("clk = 0;                                                                           ")
        self.test_code.append("rst = 0;                                                                           ")
        self.test_code.append("#100 rst =1;                                                                       ")
        self.test_code.append("end                                                                                ")
        self.test_code.append("always #1 clk= ~clk;                                                               ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("    // Inputs                                                                         ")
        self.test_code.append("    reg signed [size_a-1:0] a;                                                        ")
        self.test_code.append("    reg signed  [size_b-1:0] b;                                                       ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("    // Outputs                                                                        ")
        self.test_code.append("    wire [size_a+size_b-1:0] out1;                                                    ")
        self.test_code.append("    wire [size_a+size_b-1:0] out2;                                                    ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("    // Instantiate the Unit Under Test (UUT)                                          ")
        self.test_code.append("    multiply"+str(a)+"x"+str(b)+" uut (                                                               ")
        self.test_code.append("        .out1(out1),                                                                    ")
        self.test_code.append("        .out2(out2),                                                                    ")
        self.test_code.append("        .a(a),                                                                          ")
        self.test_code.append("        .b(b)                                                                           ")
        self.test_code.append("    );                                                                                ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("wire ee = &b & &a;                                                                 ")
        self.test_code.append("    initial begin                                                                     ")
        self.test_code.append("        // Initialize Inputs                                                            ")
        self.test_code.append("        a = 0;                                                                          ")
        self.test_code.append("        b = 0;                                                                          ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("        // Wait 100 ns for global reset to finish                                       ")
        self.test_code.append("                                                                                   ")
        self.test_code.append("        // Add stimulus here                                                            ")
        self.test_code.append("  wait(ee);                                                                        ")
        self.test_code.append("  #100;                                                                            ")
        self.test_code.append("  $display($time, \" ####################  Test Finished !  #####################\");")
        self.test_code.append("  $stop();                                                          ")
        self.test_code.append("    end                                                                ")
        self.test_code.append("                                                                    ")
        self.test_code.append("always@(posedge clk or negedge rst)                                 ")
        self.test_code.append("if(~rst) begin                                                      ")
        self.test_code.append("a<= 0;                                                              ")
        self.test_code.append("b <= 0;                                                             ")
        self.test_code.append("end else begin                                                      ")
        self.test_code.append("if(~ee & &b) a <= a + 1;                                            ")
        self.test_code.append("b <= b + 1;                                                         ")
        self.test_code.append("end                                                                 ")
        self.test_code.append("                                                                    ")
        self.test_code.append("reg [size_a+size_b-1:0] pp;                                         ")
        self.test_code.append("always@(posedge clk or negedge rst)                                 ")
        self.test_code.append("if(~rst)  pp<=0;                                                    ")
        self.test_code.append("else pp <= out1[size_a+size_b-1:0]+ {out2[size_a+size_b-1:0],1'b0};")
        self.test_code.append("                                                                   ")
        self.test_code.append("reg signed [size_a+size_b-1:0] val;                                ")
        self.test_code.append("always@(posedge clk or negedge rst)                                ")
        self.test_code.append("if(~rst)  val<=0;                                                  ")
        self.test_code.append("else val <= a*b;                                                   ")
        self.test_code.append("                                                                   ")
        self.test_code.append("reg diff;                                                          ")
        self.test_code.append("always@(posedge clk or negedge rst)                                ")
        self.test_code.append("if(~rst) diff <= 0;                                                ")
        self.test_code.append("else diff <= pp - val;                                             ")
        self.test_code.append("                                                                   ")
        self.test_code.append("always@(posedge clk or negedge rst)                                ")
        self.test_code.append("if(rst) begin                                                      ")
        self.test_code.append("    if(val != pp) $display($time, \" Error: %h, %h\\n\",val, pp);     ")
        self.test_code.append("end                                                                ")
        self.test_code.append("                                                                   ")
        self.test_code.append("endmodule                                                          ")

        """
        
        file_object = open("D:\\multiply\\tb_mul_14x12.v", 'r')
        lines=file_object.readlines()
        for i in lines:
            if(i=="module tb_mul_14x12;\n"):
                i="module tb_mul_"+str(a)+"x"+str(b)+";\n"
            if(i=="\tmultiply14X11 uut (\n"):
                i="\tmul_"+str(a)+"x"+str(b)+" uut (\n"
            if(i=="parameter size_a = 14;\n"):
                i="parameter size_a = "+str(a)+";\n"
            if(i=="parameter size_b = 11;\n"):
                i="parameter size_b = "+str(b)+";\n"
            self.test_code.append(i)

        file_object = open(path+"\\tb_mul_"+str(a)+"x"+str(b)+".v", 'w')
        #print file_name
        for i in self.test_code:
            #print i
            file_object.write(i)
        file_object.close()
        
        
        
        
        
        