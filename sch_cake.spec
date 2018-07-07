Name: 		sch_cake
Version: 	0
Release:	1%{?dist}
Summary:	Kernel module (kmod) for sch_cake

Group:		System Environment/Kernel
License:	GPLv2 or BSD
URL:		https://github.com/dtaht/sch_cake.git

ExclusiveArch:  i586 i686 x86_64 ppc ppc64

Provides:       %{name}-kmod-common = %{version}
Requires:       %{name}-kmod >= %{version}


%description
sch_cake common files.


%prep
#Nothing to prep

%build
#Nothing to build


%install
#Nothing to install


%files
#No files included

%changelog
* Sat Jul 7 2018 Samuel Patwin <dagofthedofg@gmail.com> - 0-1
- Initial spec file
