#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : krunner
Version  : 6.0.0
Release  : 76
URL      : https://download.kde.org/stable/frameworks/6.0/krunner-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/krunner-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/krunner-6.0.0.tar.xz.sig
Summary  : Framework for providing different actions given a string query
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: krunner-data = %{version}-%{release}
Requires: krunner-lib = %{version}-%{release}
Requires: krunner-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

%package data
Summary: data components for the krunner package.
Group: Data

%description data
data components for the krunner package.


%package dev
Summary: dev components for the krunner package.
Group: Development
Requires: krunner-lib = %{version}-%{release}
Requires: krunner-data = %{version}-%{release}
Provides: krunner-devel = %{version}-%{release}
Requires: krunner = %{version}-%{release}

%description dev
dev components for the krunner package.


%package lib
Summary: lib components for the krunner package.
Group: Libraries
Requires: krunner-data = %{version}-%{release}
Requires: krunner-license = %{version}-%{release}

%description lib
lib components for the krunner package.


%package license
Summary: license components for the krunner package.
Group: Default

%description license
license components for the krunner package.


%prep
%setup -q -n krunner-6.0.0
cd %{_builddir}/krunner-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709313456
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709313456
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/krunner
cp %{_builddir}/krunner-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/krunner/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/krunner-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/krunner/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/krunner-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/krunner/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/krunner-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/krunner/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/krunner-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/krunner/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/krunner-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/krunner/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/krunner-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/krunner/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/krunner-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/krunner/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/krunner-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/krunner/680295cd7d254d11edba2a4e8afd7810c79925d2 || :
cp %{_builddir}/krunner-%{version}/autotests/plugins/metadatafile1.json.license %{buildroot}/usr/share/package-licenses/krunner/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/krunner-%{version}/templates/runner6/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/krunner/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf6_org.kde.krunner1.xml
/usr/share/kdevappwizard/templates/runner6.tar.bz2
/usr/share/kdevappwizard/templates/runner6python.tar.bz2
/usr/share/qlogging-categories6/krunner.categories
/usr/share/qlogging-categories6/krunner.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KRunner/KRunner/AbstractRunner
/usr/include/KF6/KRunner/KRunner/AbstractRunnerTest
/usr/include/KF6/KRunner/KRunner/Action
/usr/include/KF6/KRunner/KRunner/QueryMatch
/usr/include/KF6/KRunner/KRunner/ResultsModel
/usr/include/KF6/KRunner/KRunner/RunnerContext
/usr/include/KF6/KRunner/KRunner/RunnerManager
/usr/include/KF6/KRunner/KRunner/RunnerSyntax
/usr/include/KF6/KRunner/krunner/abstractrunner.h
/usr/include/KF6/KRunner/krunner/abstractrunnertest.h
/usr/include/KF6/KRunner/krunner/action.h
/usr/include/KF6/KRunner/krunner/krunner_export.h
/usr/include/KF6/KRunner/krunner/querymatch.h
/usr/include/KF6/KRunner/krunner/resultsmodel.h
/usr/include/KF6/KRunner/krunner/runnercontext.h
/usr/include/KF6/KRunner/krunner/runnermanager.h
/usr/include/KF6/KRunner/krunner/runnersyntax.h
/usr/include/KF6/KRunner/krunner_version.h
/usr/lib64/cmake/KF6Runner/KF6KRunnerMacros.cmake
/usr/lib64/cmake/KF6Runner/KF6RunnerConfig.cmake
/usr/lib64/cmake/KF6Runner/KF6RunnerConfigVersion.cmake
/usr/lib64/cmake/KF6Runner/KF6RunnerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Runner/KF6RunnerTargets.cmake
/usr/lib64/libKF6Runner.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Runner.so.6.0.0
/usr/lib64/libKF6Runner.so.6
/usr/lib64/libKF6Runner.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/krunner/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/krunner/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/krunner/680295cd7d254d11edba2a4e8afd7810c79925d2
/usr/share/package-licenses/krunner/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/krunner/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/krunner/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/krunner/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/krunner/ea97eb88ae53ec41e26f8542176ab986d7bc943a
/usr/share/package-licenses/krunner/fa05e58320cb7c64786b26396f4b992579a628bc
