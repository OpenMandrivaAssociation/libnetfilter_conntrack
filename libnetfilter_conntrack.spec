%ifarch %{arm}
# Workaround for compile error (ld crash) on armv7hl
# clang 7.0-331886, binutils 2.30
%global _disable_lto 1
%endif

%define debug_package %nil
%define major	3
%define libname	%mklibname netfilter_conntrack %{major}
%define devname	%mklibname netfilter_conntrack -d

Summary:	Interface to the in-kernel connection tracking state table
Name:		libnetfilter_conntrack
Version:	1.0.8
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
# macro not ready yet
#% setup_linker_bfd
%configure
%make
# LD="%{_bindir}/ld.bfd" LDFLAGS="%{ldflags} -fuse-ld=bfd"

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libnetfilter_conntrack.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
