%global gitcommit_full eefc13513083b5daddc323f39bf0976a3fc5bc7a
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20190118

%global debug_package %{nil}

Name:           falkon-pdfreader
Version:        0
Release:        0.1.%{date}git%{gitcommit}%{?dist}
Summary:        PDF reader extension for Falkon using pdf.js

License:        GPLv3+ and ASL 2.0
URL:            https://github.com/Tarptaeya/PDFReader
Source0:        %{url}/tarball/%{gitcommit_full}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

Requires:       falkon

%description
%{summary}.

%prep
%autosetup -n Tarptaeya-PDFReader-%{gitcommit}


%build
mkdir build
pushd build
    %cmake_kf5 ..
popd


%install
pushd build
    %make_install
popd
mv pdfreader/pdfjs/LICENSE LICENSE_pdfjs


%files
%license LICENSE LICENSE_pdfjs
%doc README.md
%{_kf5_qtplugindir}/falkon/qml/pdfreader



%changelog
* Mon Mar  4 2019 Vasiliy Glazov <vascom2@gmail.com> - 0-0.1.20190118giteefc135
- Initial packaging
