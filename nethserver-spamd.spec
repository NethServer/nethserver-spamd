Name:		nethserver-spamd
Version: 1.0.1
Release: 1%{?dist}
Summary:	NethServer spamd
Group:		Networking/Daemons
License:	GPLv2
URL:		http://www.nethesis.it
Source0:	%{name}-%{version}.tar.gz
BuildArch: 	noarch

BuildRequires:	nethserver-devtools
Requires:      spamassassin


%description
Spamd daemon running under NethServer

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf %{buildroot}

%pre

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Jul 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- spam score not applied for getmail - Bug NethServer/dev#5315

* Mon Aug 08 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Replace Fetchmail with getmail - NethServer/dev#5021

