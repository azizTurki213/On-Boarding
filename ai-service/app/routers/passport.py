from fastapi import APIRouter, UploadFile, File

from app.schemas import PassportExtractionResult

router = APIRouter(prefix="/extract/passport", tags=["passport"])


@router.post("", response_model=PassportExtractionResult)
async def extract_passport(image: UploadFile = File(...)) -> PassportExtractionResult:
    """
    Phase 2 TODO (see roadmap):
      1. Read image bytes, decode with OpenCV.
      2. Locate + crop the MRZ region (bottom of the bio page).
      3. Run OCR (Tesseract/PassportEye) on the MRZ region.
      4. Parse with the `mrz` library -> fields + check-digit validation.
      5. Return a populated PassportExtractionResult.

    Stub for now so the Spring Boot integration can be wired and tested end-to-end
    before the real CV/OCR pipeline exists.
    """
    _ = await image.read()  # placeholder read so the upload contract is exercised
    return PassportExtractionResult(
        document_number="STUB0000000",
        surname="DOE",
        given_names="JANE",
        nationality="TUN",
        date_of_birth="1998-04-12",
        sex="F",
        expiry_date="2030-01-01",
        checksum_valid=None,
        overall_confidence=0.0,
    )
