#!/usr/bin/env python3
"""Download Wave 3 + fixed assets from S3 presigned URLs."""
import urllib.request, os, sys

IMG = "content-hub/assets/images"
VID = "content-hub/assets/videos"
os.makedirs(IMG, exist_ok=True)
os.makedirs(VID, exist_ok=True)

ASSETS = [
    # (dest_dir, filename, s3url)
    (IMG, "village-map-prints_small-town-plaza-grid.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/0ac9ebd0fb803d119ec5b7e0e4abf2c0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175031Z&X-Amz-Expires=3600&X-Amz-Signature=5b5a5840d34881367071dcbcb0d5a287594b8ac8586d8664f83bb0ace3585633&X-Amz-SignedHeaders=host"),
    (IMG, "gift-that-carries-home_latin-city-med-vibes-30deg.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/a4a08f3d7ba9527f7401f435c4cb3756?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175032Z&X-Amz-Expires=3600&X-Amz-Signature=99641815114de8ad32f95a58d9456d12ce7e49e63bf86438d00b32656a839157&X-Amz-SignedHeaders=host"),
    (IMG, "gift-that-carries-home_print-wall-mockup.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/5303a215a0a7e88cc184de68337b972b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175031Z&X-Amz-Expires=3600&X-Amz-Signature=6c11b80b1ee2d94df6ab92af6d3771268e059d3298028153528b3af11293227c&X-Amz-SignedHeaders=host"),
    (IMG, "bearing-says-about-you_medellin-4-bearings.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/7bcf5bb4f1b5b28e606f5c421ac19e78?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175031Z&X-Amz-Expires=3600&X-Amz-Signature=2fa01707bf84367e2801c3be0ca70734f9f3274976907039f26e2e01a9825373&X-Amz-SignedHeaders=host"),
    (VID, "bearing-says-about-you_medellin-bearing-drag.mp4",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/2c0166ce5913e9eb42b39d8b1941e191?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175034Z&X-Amz-Expires=3600&X-Amz-Signature=37e0f47c6bd563699d44feaac0069d4b000fa4fe68ee467b3089c24a1cafa939&X-Amz-SignedHeaders=host"),
    (IMG, "theme-guide_caracas-med-vibes-30deg.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/0864194c1762f35fd8baeae8c337cb69?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175034Z&X-Amz-Expires=3600&X-Amz-Signature=214ea76cb02c44e3fc13ebc7664ccabe52cc5d2d0b0c85e9a0a26b6a056f1f8b&X-Amz-SignedHeaders=host"),
    (IMG, "theme-guide_caracas-vintage-noir-30deg.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/c78755e464c5a0f0bf4fa327e060f911?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175034Z&X-Amz-Expires=3600&X-Amz-Signature=4380c6b4180d96d2de270a8c16f39cee521d0243712d52ef221eeee0d99a3e27&X-Amz-SignedHeaders=host"),
    (IMG, "theme-guide_med-vibes-vs-vintage-noir.png",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/0bfcf0b6bb0268a6b41001cf2a5da192?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175034Z&X-Amz-Expires=3600&X-Amz-Signature=a62432ff234e2ba39824debdb44bc512ee78b2f055553bacb10d82d25bf71275&X-Amz-SignedHeaders=host"),
    (VID, "theme-guide_caracas-theme-speedrun.mp4",
     "https://temp.4d4f16c61d89ec64e760039c4ec50717.r2.cloudflarestorage.com/243085/googledrive/GOOGLEDRIVE_DOWNLOAD_FILE/response/131351dd50f2d379d6f986fd4fbed2d0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a972c0e6c710f42db4e67fe0ce139aa0%2F20260508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T175036Z&X-Amz-Expires=3600&X-Amz-Signature=e00166f6695870c56c80ed6b0d066fa6e40b9e650c266904766f22da8e6314ab&X-Amz-SignedHeaders=host"),
]

for dest_dir, filename, url in ASSETS:
    dest = os.path.join(dest_dir, filename)
    try:
        urllib.request.urlretrieve(url, dest)
        size = os.path.getsize(dest)
        print(f"  ✓ {filename} ({size:,} bytes)")
    except Exception as e:
        print(f"  ✗ {filename}: {e}", file=sys.stderr)

print("Done.")
