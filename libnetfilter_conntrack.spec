%define major 3
%define libname %mklibname netfilter_conntrack %{major}
%define develname %mklibname netfilter_conntrack -d

Summary:	Interface to the in-kernel connection tracking state table
Name:		libnetfilter_conntrack
Version:	1.0.1
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://www.netfilter.org/projects/%{name}/
Source0:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2.sig
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

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}*.h
%{_includedir}/%{name}/linux_nfnetlink_conntrack.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun May 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1
+ Revision: 799736
- 1.0.1

* Mon Apr 16 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3
+ Revision: 791292
- rebuild
- rebuild
- make sure it backports, something that's totally neglected in the current rpm development frenzy

* Mon Apr 16 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2
+ Revision: 791224
- various fixes

* Sun Feb 19 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1
+ Revision: 777365
- update to new version 1.0.0

* Thu Mar 03 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.9.1-1
+ Revision: 641469
- Updated to 0.9.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.101-2mdv2011.0
+ Revision: 609763
- rebuild

* Sat Feb 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.101-1mdv2010.1
+ Revision: 512437
- bump major to 3
- obsolete old library
- drop patch0
- update to new version 0.0.101
- spec file clean

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0.0.99-2mdv2010.0
+ Revision: 438718
- rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix build with -Werror=format-security

* Thu Jan 08 2009 Jérôme Soyer <saispo@mandriva.org> 0.0.99-1mdv2009.1
+ Revision: 327170
- New upstream version
  Fix -Werror=format-security error

* Sun Dec 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.98-1mdv2009.1
+ Revision: 311656
- update to new version 0.0.98

* Sat Aug 16 2008 Funda Wang <fwang@mandriva.org> 0.0.96-1mdv2009.0
+ Revision: 272610
- fix BR
- obsoletes old devel package

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 0.0.96
    - new license policy
    - update file list
    - use macros
    - spec file clean
    - run ldconfig on %%post and %%postun for mdv versions older than 2009.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jan 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.0.82-1mdv2008.1
+ Revision: 144878
- New release

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Michael Scherer <misc@mandriva.org> 0.0.81-1mdv2008.1
+ Revision: 97579
- update to 0.0.81

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Sun May 27 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.0.31-2mdv2008.0
+ Revision: 31704
- force rebuild


* Thu Nov 16 2006 Olivier Blin <oblin@mandriva.com> 0.0.31-1mdv2007.0
+ Revision: 84793
- initial libnetfilter_conntrack release
- Create libnetfilter_conntrack

