#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-execnet
Version  : 2.0.0
Release  : 82
URL      : https://files.pythonhosted.org/packages/4f/bf/3aeb4f24c300b992d4e9db7ec1a6977c1fe1be16fef879a9f24e7b43fc1e/execnet-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4f/bf/3aeb4f24c300b992d4e9db7ec1a6977c1fe1be16fef879a9f24e7b43fc1e/execnet-2.0.0.tar.gz
Summary  : execnet: rapid multi-Python deployment
Group    : Development/Tools
License  : MIT
Requires: pypi-execnet-license = %{version}-%{release}
Requires: pypi-execnet-python = %{version}-%{release}
Requires: pypi-execnet-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
execnet: distributed Python deployment and communication
========================================================

%package license
Summary: license components for the pypi-execnet package.
Group: Default

%description license
license components for the pypi-execnet package.


%package python
Summary: python components for the pypi-execnet package.
Group: Default
Requires: pypi-execnet-python3 = %{version}-%{release}

%description python
python components for the pypi-execnet package.


%package python3
Summary: python3 components for the pypi-execnet package.
Group: Default
Requires: python3-core
Provides: pypi(execnet)

%description python3
python3 components for the pypi-execnet package.


%prep
%setup -q -n execnet-2.0.0
cd %{_builddir}/execnet-2.0.0
pushd ..
cp -a execnet-2.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688743848
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-execnet
cp %{_builddir}/execnet-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-execnet/82dbfd684f7c04da81d4faa852c6317142daa3e7 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-execnet/82dbfd684f7c04da81d4faa852c6317142daa3e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
