#!/usr/bin/env python3
"""Download Drive assets from S3 presigned URLs → assets/images/"""
import urllib.request
import os
import sys

TARGET = "content-hub/assets/images"
os.makedirs(TARGET, exist_ok=True)

# (filename, s3url)
ASSETS = [
    ("expat-memento_before-after-bearing.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/d8b572afa368d5d3b47b03b114037b85?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162442Z&X-Amz-Expires=3600&X-Amz-Signature=81c5c93d99f67c99160f21328c3c72ec0332ee894479b4655a0a5284cf97cb0e&X-Amz-SignedHeaders=host"),
    ("expat-memento_caracas-chacao-0deg-med-vibes.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/7456ce209ea350abdd99781836b2fd08?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162442Z&X-Amz-Expires=3600&X-Amz-Signature=10e3713564483358b19c15c9f19050c1504b62c53858e1ff62c431aaa695cf26&X-Amz-SignedHeaders=host"),
    ("expat-memento_caracas-chacao-30deg-med-vibes.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/6e5305e633f862c6f6df9b8652d30817?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162442Z&X-Amz-Expires=3600&X-Amz-Signature=d26ca3bd897b60ae3767c463ffb12763d0579de2542b1431a9b951dff0c37b48&X-Amz-SignedHeaders=host"),
    ("expat-memento_print-mockup.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/20e2ccdbe9567b81423f690235149862?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162442Z&X-Amz-Expires=3600&X-Amz-Signature=80d3cc2b9d5f1df0242767ab32e02950f88de34c4cecafe7de0608b7b7066f29&X-Amz-SignedHeaders=host"),
    ("expat-memento_sao-paulo-vila-madalena-30deg.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/82967353b2c228531f393c031b3e0f3d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162444Z&X-Amz-Expires=3600&X-Amz-Signature=091b1b6c8e42dfc373a76c5580f1b382492ea5bbf1c32ed63f5336e3b74109a3&X-Amz-SignedHeaders=host"),
    ("village-zoom-demo.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/522216f5078514ab6760017df0b30caa?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162444Z&X-Amz-Expires=3600&X-Amz-Signature=732953472c9a3d301acf1f026e32339738589c1d68f1d1d6319ab0eac10d8b9c&X-Amz-SignedHeaders=host"),
    ("village-map-prints_small-town-plaza-grid.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/d4ec17031315c1e7f9d547a6bf30d8eb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162444Z&X-Amz-Expires=3600&X-Amz-Signature=45c5b95f5285b18fd901fd70fac13e1ac2b468d806d784df87a8a88a486742bc&X-Amz-SignedHeaders=host"),
    ("bearing-control-ui.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/48a23784f1ea5c31306273104e34d26f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162444Z&X-Amz-Expires=3600&X-Amz-Signature=dea3ff4f20022d68dec93c601817092f494749e8658b6b6b985cd1cc14bb098e&X-Amz-SignedHeaders=host"),
    ("bearing-grid-sao-paulo.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/d7298e99208d444e420e86cd21e86dca?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162445Z&X-Amz-Expires=3600&X-Amz-Signature=5f7da041f6b2359a67fe4ab6c1f81ad8b4890440437b35de714048b3c4816365&X-Amz-SignedHeaders=host"),
    ("bearing-grid-sao-paulo.gif",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/47b8a31517b13ba15453d93f244a0c2e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162445Z&X-Amz-Expires=3600&X-Amz-Signature=7e4445c10a49b2b3389d03381231b52e8e166c425753db498919138e159943dd&X-Amz-SignedHeaders=host"),
    ("grid-brasilia.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/b9c42410a43d49b338874cfa98a64358?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162445Z&X-Amz-Expires=3600&X-Amz-Signature=b9542c36e598365b1b2cc4f06081fa2f81b343ebc87d601505e627362d6c6f85&X-Amz-SignedHeaders=host"),
    ("grid-brasilia-45deg.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/a12b9af33e8f7c5e6f282cbba6ef1eeb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162445Z&X-Amz-Expires=3600&X-Amz-Signature=dde95f81eabdb76e4789d82c5e35797a042cd30420971a3b0741c8ab4c267042&X-Amz-SignedHeaders=host"),
    ("grid-la-plata.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/9bfbd42abb5e79a17a621bf6baf61aad?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162447Z&X-Amz-Expires=3600&X-Amz-Signature=6c934bf5e85a88a81d19aa7c895dfd58a27d14f6a3e1a71d474875696279ac2b&X-Amz-SignedHeaders=host"),
    ("grid-la-plata-30deg.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/938b3af41818e73a98cbb94629699a75?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162447Z&X-Amz-Expires=3600&X-Amz-Signature=a29113f252efeb7fef28d3bab9237a1aabc936028ba1e032b19cb4683cf96714&X-Amz-SignedHeaders=host"),
    ("theme-grid-caracas.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/562bc4359985e82bb2dc990128bbaf04?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T162447Z&X-Amz-Expires=3600&X-Amz-Signature=8499f615ee9592ec28e1e3f9892b18880b0ea3ffe7f8fe6f22972a1f81dc814d&X-Amz-SignedHeaders=host"),
]

ok = []
failed = []
for filename, url in ASSETS:
    dest = os.path.join(TARGET, filename)
    try:
        urllib.request.urlretrieve(url, dest)
        size = os.path.getsize(dest)
        flag = " ⚠️  TINY" if size < 5000 else ""
        print(f"  ✓ {filename} ({size:,} bytes){flag}")
        ok.append(filename)
    except Exception as e:
        print(f"  ✗ {filename}: {e}", file=sys.stderr)
        failed.append(filename)

print(f"\n{len(ok)}/15 downloaded. {len(failed)} failed.")
if failed:
    print("Failed:", failed)
