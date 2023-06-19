%define date 20230620

Name: repodata-tools
Version: 0.0.1
Release: %{?date:0.%{date}.}1
Source0: https://github.com/OpenMandrivaSoftware/repodata-tools/archive/refs/heads/master.tar.gz#/%{name}-%{date}.tar.gz
Summary: Tools for working with rpm repomd data
URL: https://github.com/OpenMandrivaSoftware/repodata-tools
License: AGPL-3.0+
Group: System/Configuration/Packaging
BuildRequires: cmake ninja
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Xml)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(rpm)

%description
Tools for working with rpm repomd data

%prep
%autosetup -p1 -n %{name}-%{?date:master}%{!?date:%{version}}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/createmd
