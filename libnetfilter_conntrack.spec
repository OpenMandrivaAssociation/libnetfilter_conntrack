%define debug_package %nil
%define major 3
%define libname	%mklibname netfilter_conntrack %{major}
%define devname	%mklibname netfilter_conntrack -d

# (tpg) optimize it a bit
%global optflags %{optflags} -Oz

Summary:	Interface to the in-kernel connection tracking state table
Name:		libnetfilter_conntrack
Version:	1.0.9
Release:	3
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		https://www.netfilter.org/projects/%{name}/
Source0:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libnfnetlink)
BuildRequires:	pkgconfig(libmnl)
Obsoletes:	libnetfilter_conntrack3  < 1.0.9-2
Obsoletes:	libnetfilter_conntrack-devel < 1.0.9-2

%description
A libnetfilter_conntrack is a userspace library providing a programming \
interface (API) to the in-kernel connection tracking state table.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

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
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libnetfilter_conntrack.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
