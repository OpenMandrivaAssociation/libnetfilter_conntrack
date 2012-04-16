%define major 3
%define libname %mklibname netfilter_conntrack %{major}
%define develname %mklibname netfilter_conntrack -d

Summary:	Interface to the in-kernel connection tracking state table
Name:		libnetfilter_conntrack
Version:	1.0.0
Release:	2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.netfilter.org/projects/%{name}/
Source0:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
BuildRequires:	nfnetlink-devel >= 1.0.0

%description
A libnetfilter_conntrack is a userspace library providing a programming \
interface (API) to the in-kernel connection tracking state table.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname netfilter_conntrack 1} < 0.0.101

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	netfilter_conntrack-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d netfilter_conntrack 1}

%description -n %{develname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}*.h
%{_includedir}/%{name}/linux_nfnetlink_conntrack.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
