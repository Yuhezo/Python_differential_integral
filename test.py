import sympy as sp
from sympy.abc import x,y

def main():
    print("미분과 적분을 해주는 프로그램입니다.")
    choice = input("미분 또는 적분 중 선택하세요 : ")
    
    if choice == "미분" :
        print("미분을 선택하셨습니다.")
        choice = input("편미분 (x만 있는 함수) 과 전미분 (x와 y가 있는 함수) 중 하나를 선택하세요. : ")
        
        if choice == "편미분" :
            print("편미분을 선택하셨습니다.")
            function_x = input("x로 이루어진 함수를 쓰세요. (예시 : x**3 + 2*x**2 + 4*x + 3) : ")
            미분결과 = sp.diff(sp.sympify(function_x), x)
            print ("미분 결과 :" , 미분결과)

            while True:
                답변 = input("한번 더 미분 하시겠습니까? 답변 Y/N (대문자) : ")
            
                if 답변 == "Y":
                    미분결과 = sp.diff(sp.sympify(미분결과), x)     
                    print("미분 결과 :", 미분결과)

                elif 답변 == "N":
                    break
                
                else:
                    print("잘못된 입력입니다. 'Y' 또는 'N' 중 하나를 입력해주세요.")
         
        elif choice == "전미분" :
            print("전미분을 선택하셨습니다.")
            function_xy = input("x와 y로 이루어진 함수를 쓰세요. (예시 : x**3 + 3*y**2 + 4*y + 2) : ")
            choice = input("dy/dx 또는 dx/dy 를 선택하세요. : ")
                
            if choice == "dy/dx" :
                print("dy/dx를 선택하셨습니다.")
                미분결과1 = sp.idiff(sp.sympify(function_xy), y, x)
                print("미분 결과 :" , 미분결과1)
            
            elif choice == "dx/dy" :
                print("dx/dy를 선택하셨습니다.")
                미분결과2 = sp.idiff(sp.sympify(function_xy), x, y)
                print("미분 결과 :" , 미분결과2)

            else:
                print("잘못된 입력입니다. 'dy/dx' 또는 'dx/dy' 중 하나를 입력해주세요.")   

        else:
            print("잘못된 입력입니다. '편미분' 또는 '전미분' 중 하나를 입력해주세요.")    

        
    elif choice == "적분":
        print("적분을 선택하셨습니다.")
        function_integral = input("x로 이루어진 함수를 쓰세요. (예시 : 3*x**2 + 4*x +2) : ")
        적분결과 = sp.integrate(sp.sympify(function_integral), x)
        print("적분 결과 :" , 적분결과)
    
    else:
        print("잘못된 입력입니다. '미분' 또는 '적분' 중 하나를 입력해주세요.")
    
    input("프로그램을 종료하려면 Enter를 누르세요...")
    
if __name__ == "__main__":
    main()
