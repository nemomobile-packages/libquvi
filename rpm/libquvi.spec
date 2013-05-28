Name:           libquvi
Version:        0.4.1
Release:        1
Summary:        Library for parsing video download links
Group:          Development/Libraries
License:        LGPLv2+
URL:            http://quvi.sourceforge.net/
Source0:        http://heanet.dl.sourceforge.net/project/quvi/0.4/%{name}/%{name}-%{version}.tar.xz
Patch0:	        woarkaround-old-automake.patch
Requires:       libquvi-scripts
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libquvi-scripts)

%description
 Library to parse Adobe flash video download links. It supports Youtube
 and other similar video websites. It provides access to functionality and
 data through an API, and does not enable or require the use of the
 flash technology.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1

%build
%autogen 
%configure --disable-static
./gen-ver.sh > VERSION
touch ChangeLog

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*
