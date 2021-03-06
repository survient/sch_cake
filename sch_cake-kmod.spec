%global buildforkernels akmod
%global commit c91b94f0b4456c43def2e77248a455a9a2449ed1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20180706
%global debug_package %{nil}

Name: 		sch_cake-kmod
Version:	0
Release:	0.1.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:	Kernel module (kmod) for sch_cake

Group:		System Environment/Kernel
License:	GPLv2 or BSD
URL:		https://github.com/dtaht/sch_cake.git
Source0:	https://github.com/dtaht/sch_cake/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:	%{_bindir}/kmodtool

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Kernel Module containing Cake queuing discipline.


%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}
# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null
%setup -qn %{name}-%{commit} -c -T -a 0
for kernel_version in %{?kernel_versions} ; do
    cp -a sch_cake-%{commit} _kmod_build_${kernel_version%%___*}
done


%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" SUBDIRS=${PWD}/_kmod_build_${kernel_version%%___*} modules
    %make_build -C "${kernel_version##*___}" SUBDIRS=${PWD}/_kmod_build_${kernel_version%%___*} modules
done


%install
for kernel_version in %{?kernel_versions}; do
    install -D -m 755 -t ${buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/ $(find _kmod_build_${kernel_version%%___*}/ -name '*.ko')
    chmod u+x %{buildroot}%{_prefix}/lib/modules/*/extra/*/*
done
%{?akmod_install}


%changelog
* Sun Jul 8 2018 Samuel Patwin <dagofthedofg@gmail.com> - 0-0.1.20180706gitc91b94f
- Initial spec file
