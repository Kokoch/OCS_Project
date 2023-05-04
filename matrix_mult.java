/* This program aims to multiplie to matrices together, source: https://www.javatpoint.com/java-program-to-multiply-two-matrices*/

public class Matrix_Mult{  
    public static void main(String args[]){  

    // creates the first matrix and assigns its initial values
    int a[][]={{1,1,1},{2,2,2},{3,3,3}};   
    
    // creates the second matrix and assigns its initial values
    int b[][]={{1,1,1},{2,2,2},{3,3,3}};    
        
    // creates another matrix to store the multiplication of the two matrices    
    int c[][]=new int[3][3];  // here we assume that we hardcode the size of 3 rows and 3 columns, maybe we will treat all figure cases later on like 2x4 
        
    // multiplying and printing multiplication of 2 matrices    
    for(int i=0;i<3;i++){    
        for(int j=0;j<3;j++){    
            c[i][j]=0;      
            for(int k=0;k<3;k++) {      
                c[i][j]+=a[i][k]*b[k][j];      
            }//end of k loop  
            System.out.print(c[i][j]+" ");  //printing matrix element  
        }//end of j loop  
        System.out.println();//new line    
    }    
    }
}  