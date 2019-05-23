TooresAna_final_15.pdf: %.dat
	python plot.py 
    
all: datos.dat

%.dat: sol.x
	./sol.x

sol.x: sol.cpp
	c++ sol.cpp -o sol.x

clean:
	rm -rf *.x *.dat
    