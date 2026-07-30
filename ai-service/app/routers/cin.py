from fastapi import APIRouter, UploadFile, File

from app.schemas import CinExtractionResult

router = APIRouter(prefix="/extract/cin", tags=["cin"])


@router.post("", response_model=CinExtractionResult)
async def extract_cin(image: UploadFile = File(...)) -> CinExtractionResult:
    """
    Phase 3 TODO (see roadmap):
      1. Read image bytes, decode with OpenCV.
      2. Detect/crop/deskew the card (contour detection first).
      3. Normalize to a fixed reference size so field regions line up.
      4. OCR each pre-defined field region independently (PaddleOCR, ar+fr).
      5. Validate each field (date formats, ID number pattern) and compute
         a per-field confidence -> overall_confidence.

    Stub for now so the Spring Boot integration can be wired and tested end-to-end
    before the real CV/OCR pipeline exists.
    """
    _ = await image.read()
    return CinExtractionResult(
        document_number="STUB0000000",
        last_name="DOE",
        first_name="JANE",
        date_of_birth="1998-04-12",
        place_of_birth="Tunis",
        address="Tunis",
        overall_confidence=0.0,
    )
