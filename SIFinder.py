king_1= """
A Simple Interest Chapter Solver
si    >> To find Simple Interest 
am  >> To find Amount
p      >> To find Principal 
r      >> To find rate
"""

print(king_1)






bh1=True
while bh1==True:
	try:
		m_e=input("Enter a Method\n")
#To Find Interest 

		if m_e=="si":
			try:
				a_1=int(input("Enter Principal\n"))
				a_2=int(input("Enter Time Numerator\n"))
				p_5=int(input("Enter Time Denominator\n"))
				p_r=(a_2/p_5)
				a_3=int(input("Enter Rate\n"))
				p_g=(a_1*p_r*a_3)/100
				ru_1="₹"
				p_gi=str(p_g)
				d_1="Interest is "
				print(d_1 +p_gi+ str(ru_1))
				y_4=input("Enter yes/No to continue\n").lower()
				if y_4=="yes":
					continue 
				else:
					break
			except:
				print("Enter only numeric value")	
#To find Amount

		elif m_e=="am":
			try:
				a_1=int(input("Enter Principal\n"))
				a_2=int(input("Enter Time Numerator\n"))
				p_5=int(input("Enter Time Denominator\n"))
				p_r=(a_2/p_5)
				a_3=int(input("Enter Rate\n"))
				p_g=(a_1*p_r*a_3)/100
				a_m=(p_g+a_1)
				s_8=str(a_m)
				r_5="₹"
				p_go=str(a_m)
				d_2="Amount is "
				a_m1=(d_2 +p_go+r_5)
				print(a_m1)
				y_3=input("Enter yes/No to continue\n").lower()
				if y_3=="yes":
					continue 
				else:
					break
			except:
				print("Enter Numeric value")
#To find principal 

		elif m_e=="p":
			try:
				a_1=int(input("Enter Interest\n"))
				a_2=int(input("Enter Time Numerator \n"))
				p_5=int(input("Enter Time denominator \n"))
				p_r=(a_2/p_5)
				a_3=int(input("Enter Rate\n"))
				p_g5=(100*a_1)/(a_3*p_r)
				fl=int(p_g5)
				ru_1="₹"
				p_gi=str(p_g5)
				print(p_gi+str(ru_1))
				y_2=input("Enter yes/No to continue\n").lower()
				if y_2=="yes":
					continue 
				else:
					break
			except:
				print("Enter Numeric value")
#To find Rate
			
		elif m_e=="r":
				r_a=float(input("Enter Interest\n"))
				r_b=int(input("Enter Principal\n"))
				r_c=int(input("Enter Time numerator\n"))
				r_d=int(input("Enter Time denominator\n"))
				r_dc=(r_c/r_d)
				p_r=(100*r_a)/(r_b*r_dc)
				print(p_r)
				y_1=input("Enter yes/No to continue\n").lower()
#For asking to Continue or Exit
	
				if y_1=="yes":
					continue 
				else:
					break
		
	except :
		print("Error!")