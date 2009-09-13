%define major 1
%define libname %mklibname netfilter_conntrack %{major}
%define develname %mklibname netfilter_conntrack -d

Summary:	Interface to the in-kernel connection tracking state table
Name:		libnetfilter_conntrack
Version:	0.0.99
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.netfilter.org/projects/%{name}/
Source0:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
Patch0:     libnetfilter_conntrack-fix-string-error.patch
BuildRequires:	nfnetlink-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A libnetfilter_conntrack is a userspace library providing a programming \
interface (API) to the in-kernel connection tracking state table.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d netfilter_conntrack 1}

%description -n %{develname}
This package contains the development files for %{name}.

%prep
%setup -q
%patch0 -p1
%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}*.h
%{_includedir}/%{name}/linux_nfnetlink_conntrack.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}.a
%{_libdir}/%{name}.la
%{_libdir}/pkgconfig/%{name}.pc
