%define lib_rname netfilter_conntrack
%define name lib%{lib_rname}
%define version 0.0.81
%define release %mkrel 1

%define common_description libnetfilter_conntrack is a userspace library providing a programming \
interface (API) to the in-kernel connection tracking state table.

%define lib_major       1
%define lib_name_orig   %mklibname %{lib_rname}
%define lib_name        %{lib_name_orig}%{lib_major}

Summary: Interface to the in-kernel connection tracking state table
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.netfilter.org/projects/%{name}/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libnfnetlink-devel

%description
%{common_description}

%package -n %{name}-utils
Summary:        Utilities for %{name}
Group:          System/Kernel and hardware
Provides:       %{lib_name_orig} = %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n %{name}-utils
%{common_description}

This package contains utilities for %{name}.

%package -n %{lib_name}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{lib_name_orig} = %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n %{lib_name}
%{common_description}

This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{lib_name}-devel
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name} = %{version}-%{release}
Provides:       %{lib_name_orig}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name}-devel
%{common_description}

This package contains the development files for %{name}.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/%{name}.so.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.a
%{_libdir}/%{name}/*.la
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{lib_name}-devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}*.h
%{_includedir}/%{name}/linux_nfnetlink_conntrack.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}.a
%{_libdir}/%{name}.la

#%files -n %{name}-utils
#%defattr(-,root,root)
#%{_bindir}/*


