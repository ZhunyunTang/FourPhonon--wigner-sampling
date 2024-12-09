export FFLAGS=-traceback -debug -O3 ## -static_intel
export FFLAGS= -debug -O2 
export LDFLAGS=-L/home/Software/spglib/spglib-1.8.3/build/lib/libsymspg.a
export LDFLAGS=-L/home/Software/spglib/spglib-1.8.3/build/lib -lsymspg
export MPIFC=mpiifort
MKLROOT=/home/Software/intel/install/compilers_and_libraries_2019.4.243/linux/mkl
MKL=$(MKLROOT)/lib/intel64/libmkl_lapack95_lp64.a -Wl,--start-group \
$(MKLROOT)/lib/intel64/libmkl_intel_lp64.a           \
$(MKLROOT)/lib/intel64/libmkl_sequential.a           \
$(MKLROOT)/lib/intel64/libmkl_core.a -Wl,--end-group -lpthread -lm
export LAPACK=$(MKL)
export LIBS=$(LAPACK)
