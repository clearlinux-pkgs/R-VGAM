#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-VGAM
Version  : 1.1.5
Release  : 33
URL      : https://cran.r-project.org/src/contrib/VGAM_1.1-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/VGAM_1.1-5.tar.gz
Summary  : Vector Generalized Linear and Additive Models
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-VGAM-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
statistical regression models. The central algorithm is
    Fisher scoring and iterative reweighted least squares.
    At the heart of this package are the vector generalized linear
    and additive model (VGLM/VGAM) classes. VGLMs can be loosely
    thought of as multivariate GLMs. VGAMs are data-driven
    VGLMs that use smoothing. The book "Vector Generalized

%package lib
Summary: lib components for the R-VGAM package.
Group: Libraries

%description lib
lib components for the R-VGAM package.


%prep
%setup -q -c -n VGAM
cd %{_builddir}/VGAM

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610640796

%install
export SOURCE_DATE_EPOCH=1610640796
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VGAM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VGAM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VGAM
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc VGAM || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/VGAM/CITATION
/usr/lib64/R/library/VGAM/DESCRIPTION
/usr/lib64/R/library/VGAM/INDEX
/usr/lib64/R/library/VGAM/Meta/Rd.rds
/usr/lib64/R/library/VGAM/Meta/data.rds
/usr/lib64/R/library/VGAM/Meta/demo.rds
/usr/lib64/R/library/VGAM/Meta/features.rds
/usr/lib64/R/library/VGAM/Meta/hsearch.rds
/usr/lib64/R/library/VGAM/Meta/links.rds
/usr/lib64/R/library/VGAM/Meta/nsInfo.rds
/usr/lib64/R/library/VGAM/Meta/package.rds
/usr/lib64/R/library/VGAM/NAMESPACE
/usr/lib64/R/library/VGAM/NEWS
/usr/lib64/R/library/VGAM/R/VGAM
/usr/lib64/R/library/VGAM/R/VGAM.rdb
/usr/lib64/R/library/VGAM/R/VGAM.rdx
/usr/lib64/R/library/VGAM/data/Rdata.rdb
/usr/lib64/R/library/VGAM/data/Rdata.rds
/usr/lib64/R/library/VGAM/data/Rdata.rdx
/usr/lib64/R/library/VGAM/demo/binom2.or.R
/usr/lib64/R/library/VGAM/demo/cqo.R
/usr/lib64/R/library/VGAM/demo/distributions.R
/usr/lib64/R/library/VGAM/demo/lmsqreg.R
/usr/lib64/R/library/VGAM/demo/vgam.R
/usr/lib64/R/library/VGAM/demo/zipoisson.R
/usr/lib64/R/library/VGAM/help/AnIndex
/usr/lib64/R/library/VGAM/help/VGAM.rdb
/usr/lib64/R/library/VGAM/help/VGAM.rdx
/usr/lib64/R/library/VGAM/help/aliases.rds
/usr/lib64/R/library/VGAM/help/paths.rds
/usr/lib64/R/library/VGAM/html/00Index.html
/usr/lib64/R/library/VGAM/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/VGAM/libs/VGAM.so
/usr/lib64/R/library/VGAM/libs/VGAM.so.avx2
/usr/lib64/R/library/VGAM/libs/VGAM.so.avx512
