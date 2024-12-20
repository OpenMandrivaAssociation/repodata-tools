%define date 20230913

Name: repodata-tools
Version: 0.0.1
Release: %{?date:0.%{date}.}4
Source0: https://github.com/OpenMandrivaSoftware/repodata-tools/archive/refs/heads/master.tar.gz#/%{name}-%{date}.tar.gz
Source1: %{name}.rpmlintrc
Summary: Tools for working with rpm repomd data
URL: https://github.com/OpenMandrivaSoftware/repodata-tools
License: AGPL-3.0+
Group: System/Configuration/Packaging
BuildRequires: cmake ninja
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Xml)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(rpm)
# For the SVG image format plugin, so we can convert
# SVG to PNG when generating appstream metadata
Requires: %mklibname Qt6Svg

%description
Tools for working with rpm repomd data

%prep
%autosetup -p1 -n %{name}-%{?date:master}%{!?date:%{version}}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
# The non-perfile version is only for reference and may be removed altogether
mv -f %{buildroot}%{_bindir}/createmd-perfile  %{buildroot}%{_bindir}/createmd

%files
%{_bindir}/createmd
