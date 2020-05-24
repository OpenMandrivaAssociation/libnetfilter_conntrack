# libnetfilter_conntrack is used by iptables, iptables
# is used by systemd, libsystemd is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%ifarch %{arm}
# Workaround for compile error (ld crash) on armv7hl
# clang 7.0-331886, binutils 2.30
%global _disable_lto 1
%endif

%define debug_package %nil
%define major	3
%define libname	%mklibname netfilter_conntrack %{major}
%define devname	%mklibname netfilter_conntrack -d
%define lib32name libnetfilter_conntrack%{major}
%define dev32name libnetfilter_conntrack-devel

Summary:	Interface to the in-kernel connection tracking state table
Name:		libnetfilter_conntrack
Version:	1.0.8
Release:	2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.netfilter.org/projects/%{name}/
Source0:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2.sig
BuildRequires:	nfnetlink-devel >= 1.0.0
BuildRequires:	pkgconfig(libmnl)
%if %{with compat32}
BuildRequires:	devel(libmnl)
BuildRequires:	devel(libnfnetlink)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	Main library for %{name} (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{dev32name}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package contains the development files for %{name}.
%endif

%prep
%autosetup -p1
export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libnetfilter_conntrack.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libnetfilter_conntrack.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/%{name}.so
%{_prefix}/lib/pkgconfig/%{name}.pc
%endif
