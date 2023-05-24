/* This program aims to multiply two matrices together, source: https://www.javatpoint.com/java-program-to-multiply-two-matrices*/

import java.util.Random;

public class matrix {
    public static void main(String[] args) {

        // Assigns argument to size, range and type in that order.
        int m_size = Integer.parseInt(args[0]);
        int m_range = Integer.parseInt(args[1]);
        int m_type = Integer.parseInt(args[2]); // Chosen domain, O = Positive Integers, 1 = Integers, 2 = Reals. 
        
        //System.out.println("Size: " + m_size);
        //System.out.println("Range: " + m_range);
        //System.out.println("Type: " + m_type + "\n");

        // If chosen domain is N.
        if (m_type == 0) {

            // Generates a random matrix WRT to the passed in arguments.
            Random r=new Random();
            int[][] a=new int[m_size][m_size];
            for(int i=0;i<m_size;i++)
            {
                for(int j=0;j<m_size;j++)
                {
                    a[i][j]=r.nextInt(m_range);
                    //System.out.print(a[i][j]+"\t");
                }
    
                //System.out.print("\n");
            }

            // Creates another matrix to store the matrix multiplication.    
            int c[][]=new int[m_size][m_size]; 
            
            // Matrix multiplication.     
            for(int i=0;i<m_size;i++){   

                for(int j=0;j<m_size;j++){    
                    c[i][j]=0;      

                    for(int k=0;k<m_size;k++) {      
                        c[i][j]+=a[i][k]*a[k][j];      
                    }
                    
                    //System.out.print(c[i][j]+" "); 
                }

                //System.out.println();   
            }   
        }

        // If chosen domain is Z.
        if (m_type == 1) {

            // Generates a random matrix WRT to the passed in arguments.
            Random r=new Random();
            int[][] a=new int[m_size][m_size];
            for(int i=0;i<m_size;i++)
            {
                for(int j=0;j<m_size;j++)
                {
                    a[i][j]=r.nextInt(m_range/2 - -m_range/2) + -m_range/2;
                    System.out.print(a[i][j]+"\t");
                }
    
                System.out.print("\n");
            }
    
            // Creates another matrix to store the matrix multiplication.    
            int c[][]=new int[m_size][m_size];   
            
            // Matrix multiplication.     
            for(int i=0;i<m_size;i++){   

                for(int j=0;j<m_size;j++){    
                    c[i][j]=0;      

                    for(int k=0;k<m_size;k++) {      
                        c[i][j]+=a[i][k]*a[k][j];      
                    }
                    
                    //System.out.print(c[i][j]+" "); 
                }

                //System.out.println();   
            }            
        }

        // If chosen domain is R.
        if (m_type == 2) {
                        
            // Generates a random matrix WRT to the passed in arguments.
            Random r=new Random();
            float float_range = (float) m_range;
            
            float[][] a=new float[m_size][m_size];
            for(int i=0;i<m_size;i++)
            {
                for(int j=0;j<m_size;j++)
                {
                    a[i][j]=-float_range + r.nextFloat() * (float_range - -float_range);
                    System.out.print(a[i][j]+"\t");
                }
    
                System.out.print("\n");
            }
    
            // Creates another matrix to store the matrix multiplication.    
            float c[][]=new float[m_size][m_size]; 
                
            // Matrix multiplication.     
            for(int i=0;i<m_size;i++){   

                for(int j=0;j<m_size;j++){    
                    c[i][j]=0;      

                    for(int k=0;k<m_size;k++) {      
                        c[i][j]+=a[i][k]*a[k][j];      
                    }
                    
                    //System.out.print(c[i][j]+" "); 
                }

                //System.out.println();   
            }  
        }
        
 
    }
}