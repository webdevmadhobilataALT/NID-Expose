class NIDExposureEngine:

    TEST_DATASET = {
        "8268937375": [
            "Test Breach Dataset 2026",
        ],

        "1111111111": [
            "Test Breach Dataset 2026",
            "Demo Identity Dataset",
        ],

        "2222222222": [
            "Demo Identity Dataset",
        ],
    }

    @classmethod
    def check(cls, nid_number):
        """
        Check a NID against authorized test datasets.
        """

        matches = cls.TEST_DATASET.get(
            nid_number,
            [],
        )

        return {
            "is_exposed": bool(matches),
            "match_count": len(matches),
            "datasets": matches,
        }