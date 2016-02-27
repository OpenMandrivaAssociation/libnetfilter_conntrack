%define debug_package %nil
%define major	3
%define libname	%mklibname netfilter_conntrack %{major}
%define devname	%mklibname netfilter_conntrack -d

Summary:	Interface to the in-kernel connection tracking state table
Name:		libnetfilter_conntrack
Version:	1.0.5
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.netfilter.org/projects/%{name}/
Source0:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2.sig
BuildRequires:	nfnetlink-devel >= 1.0.0
BuildRequires:	pkgconfig(libmnl)

%description
A libnetfilter_conntrack is a userspace library providing a programming \
interface (API) to the in-kernel connection tracking state table.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	netfilter_conntrack-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
export CC=gcc
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libnetfilter_conntrack.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}*.h
%{_includedir}/%{name}/linux_nfnetlink_conntrack.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

