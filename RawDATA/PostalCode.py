import random, base64
API = base64.b64decode(b'WU4xNy1OSjM4LVdBMjctV1I4OA==').decode()
postalCode = """J2R 0A1
J2R 1A1
J2R 1A2
J2R 1A3
J2R 1A4
J2R 1A5
J2R 1A6
J2R 1A7
J2R 1A8
J2R 1A9
J2R 1B1
J2R 1B2
J2R 1B3
J2R 1B4
J2R 1B5
J2R 1B6
J2R 1B7
J2R 1B8
J2R 1B9
J2R 1C1
J2R 1C2
J2R 1C3
J2R 1C4
J2R 1C5
J2R 1C6
J2R 1C7
J2R 1C8
J2R 1C9
J2R 1E1
J2R 1E2
J2R 1E3
J2R 1E4
J2R 1E5
J2R 1E6
J2R 1E7
J2R 1E8
J2R 1E9
J2R 1G1
J2R 1G2
J2R 1G3
J2R 1G4
J2R 1G5
J2R 1G6
J2R 1G7
J2R 1G8
J2R 1G9
J2R 1H1
J2R 1H2
J2R 1H3
J2R 1H4
J2R 1H5
J2R 1H6
J2R 1H7
J2R 1H8
J2R 1H9
J2R 1J1
J2R 1J2
J2R 1J3
J2R 1J4
J2R 1J5
J2R 1J6
J2R 1J7
J2R 1J8
J2R 1J9
J2R 1K1
J2R 1K2
J2R 1K3
J2R 1K4
J2R 1K5
J2R 1K6
J2R 1K7
J2R 1K8
J2R 1L1
J2R 1L2
J2R 1L3
J2R 1L4
J2R 1L5
J2R 1L6
J2R 1L7
J2R 1L8
J2R 1L9
J2R 1M1
J2R 1M2
J2R 1M3
J2R 1M4
J2R 1M5
J2R 1M6
J2R 1M7
J2R 1M8
J2R 1M9
J2R 1N1
J2R 1N2
J2R 1N3
J2R 1N4
J2R 1N5
J2R 1N6
J2R 1N7
J2R 1N8
J2R 1N9
J2R 1P1
J2R 1P2
J2R 1P3
J2R 1P4
J2R 1P5
J2R 1P6
J2R 1P7
J2R 1P8
J2R 1P9
J2R 1R1
J2R 1R2
J2R 1R3
J2R 1R4
J2R 1R5
J2R 1R6
J2R 1R7
J2R 1R8
J2R 1R9
J2R 1S1
J2R 1S2
J2R 1S3
J2R 1S4
J2R 1S5
J2R 1S6
J2R 1S7
J2R 1S8
J2R 1S9
J2R 1T1
J2R 1T2
J2R 1T3
J2R 1T4
J2R 1T5
J2R 1T6
J2R 1T7
J2R 1T8
J2R 1T9
J2R 1V1
J2R 1V2
J2R 1V3
J2R 1V4
J2R 1V5
J2R 1V6
J2R 1V7
J2R 1V8
J2R 1V9
J2R 1W1
J2R 1W2
J2R 1W3
J2R 1W4
J2R 1W5
J2R 1W6
J2R 1W7
J2R 1W8
J2R 1W9
J2R 1X1
J2R 1X2
J2R 1X3
J2R 1X4
J2R 1X5
J2R 1X6
J2R 1X7
J2R 1X8
J2R 1X9
J2R 1Y1
J2R 1Y2
J2R 1Y3
J2R 1Y4
J2R 1Y5
J2R 1Y6
J2R 1Y7
J2R 1Y8
J2R 1Y9
J2R 1Z1
J2R 1Z2
J2R 1Z3
J2R 1Z4
J2R 1Z5
J2R 1Z6
J2R 1Z7
J2R 1Z8
J2R 1Z9
J2R 2A1
J2R 2A2
J2R 2A3
J2R 2A4
J2R 2A5
J2R 2A6
J2R 2A7
J2R 2A8
J2R 2A9
J2R 2B1
J2R 2B2
J2R 2B3
J2R 2B4
J2R 2B5
J2R 2B6
J2R 2B7
J2R 2B8
J2R 2B9
J2R 2C1
J2R 2C2
J2R 2C3
J2R 2C4
J2R 2C5
J2R 2C6
J2R 2C7
J2R 2C8
J2R 2C9
J2R 2E1
J2R 2E2
J2R 2E3
J2R 2E4
J2R 2E5
J2R 2E6
J2R 2E7
J2R 2E8
J2R 2E9
J2R 2G2
J2R 2G3
J2R 2G4
J2R 2G5
J2R 2G6
J2R 2G7
J2R 2G8
J2R 2G9
J2R 2H1
J2R 2H2
J2R 2H3
J2R 2H4
J2R 2H5
J2R 2H6
J2R 2H7
J2R 2H8
J2R 2H9
J2R 2J1
J2R 2J2
J2R 2J3
J2R 2J4
J2R 2J5
J2R 2J6
J2R 2J7
J2S 0A1
J2S 0A2
J2S 0A3
J2S 0A4
J2S 0A5
J2S 0A6
J2S 0A7
J2S 1A1
J2S 1A2
J2S 1A3
J2S 1A4
J2S 1A5
J2S 1A6
J2S 1A7
J2S 1A8
J2S 1A9
J2S 1B2
J2S 1B3
J2S 1B4
J2S 1B5
J2S 1B6
J2S 1B7
J2S 1B8
J2S 1B9
J2S 1C1
J2S 1C2
J2S 1C3
J2S 1C4
J2S 1C5
J2S 1C6
J2S 1C7
J2S 1C8
J2S 1C9
J2S 1E1
J2S 1E2
J2S 1E3
J2S 1E4
J2S 1E5
J2S 1E6
J2S 1E8
J2S 1E9
J2S 1G1
J2S 1G2
J2S 1G3
J2S 1G4
J2S 1G5
J2S 1G6
J2S 1G7
J2S 1G8
J2S 1G9
J2S 1H1
J2S 1H2
J2S 1H3
J2S 1H4
J2S 1H5
J2S 1H6
J2S 1H7
J2S 1H8
J2S 1H9
J2S 1J1
J2S 1J2
J2S 1J3
J2S 1J4
J2S 1J5
J2S 1J6
J2S 1J7
J2S 1J8
J2S 1J9
J2S 1K1
J2S 1K2
J2S 1K3
J2S 1K4
J2S 1K5
J2S 1K6
J2S 1K7
J2S 1K8
J2S 1K9
J2S 1L1
J2S 1L2
J2S 1L3
J2S 1L4
J2S 1L5
J2S 1L6
J2S 1L7
J2S 1L8
J2S 1L9
J2S 1M1
J2S 1M2
J2S 1M4
J2S 1M5
J2S 1M6
J2S 1M7
J2S 1M8
J2S 1M9
J2S 1N1
J2S 1N2
J2S 1N3
J2S 1N4
J2S 1N5
J2S 1N6
J2S 1N7
J2S 1N8
J2S 1N9
J2S 1P1
J2S 1P2
J2S 1P3
J2S 1P4
J2S 1P5
J2S 1P6
J2S 1P7
J2S 1P8
J2S 1P9
J2S 1R1
J2S 1R2
J2S 1R3
J2S 1R4
J2S 1R5
J2S 1R6
J2S 1R7
J2S 1R8
J2S 1R9
J2S 1S1
J2S 1S2
J2S 1S3
J2S 1S4
J2S 1S5
J2S 1S6
J2S 1S7
J2S 1S8
J2S 1S9
J2S 1T1
J2S 1T2
J2S 1T3
J2S 1T4
J2S 1T5
J2S 1T6
J2S 1T7
J2S 1T8
J2S 1T9
J2S 1V1
J2S 1V2
J2S 1V3
J2S 1V4
J2S 1V5
J2S 1V6
J2S 1V7
J2S 1V8
J2S 1V9
J2S 1W1
J2S 1W2
J2S 1W4
J2S 1W5
J2S 1W6
J2S 1W7
J2S 1W8
J2S 1W9
J2S 1X1
J2S 1X2
J2S 1X3
J2S 1X4
J2S 1X5
J2S 1X6
J2S 1X7
J2S 1X8
J2S 1X9
J2S 1Y1
J2S 1Y2
J2S 1Y3
J2S 1Y4
J2S 1Y5
J2S 1Y6
J2S 1Y7
J2S 1Y8
J2S 1Y9
J2S 1Z1
J2S 1Z2
J2S 1Z3
J2S 1Z4
J2S 1Z5
J2S 1Z6
J2S 1Z7
J2S 1Z8
J2S 1Z9
J2S 2A1
J2S 2A2
J2S 2A3
J2S 2A4
J2S 2A5
J2S 2A6
J2S 2A7
J2S 2A8
J2S 2A9
J2S 2B1
J2S 2B2
J2S 2B3
J2S 2B4
J2S 2B5
J2S 2B6
J2S 2B7
J2S 2B8
J2S 2B9
J2S 2C1
J2S 2C2
J2S 2C3
J2S 2C4
J2S 2C5
J2S 2C6
J2S 2C7
J2S 2C8
J2S 2C9
J2S 2E1
J2S 2E2
J2S 2E3
J2S 2E4
J2S 2E5
J2S 2E6
J2S 2E7
J2S 2E8
J2S 2E9
J2S 2G1
J2S 2G2
J2S 2G3
J2S 2G4
J2S 2G5
J2S 2G6
J2S 2G7
J2S 2G8
J2S 2G9
J2S 2H1
J2S 2H3
J2S 2H4
J2S 2H5
J2S 2H6
J2S 2H7
J2S 2H8
J2S 2H9
J2S 2J1
J2S 2J2
J2S 2J3
J2S 2J4
J2S 2J5
J2S 2J6
J2S 2J7
J2S 2J8
J2S 2J9
J2S 2K1
J2S 2K2
J2S 2K3
J2S 2K4
J2S 2K5
J2S 2K6
J2S 2K7
J2S 2K8
J2S 2K9
J2S 2L1
J2S 2L2
J2S 2L3
J2S 2L4
J2S 2L5
J2S 2L6
J2S 2L7
J2S 2L8
J2S 2L9
J2S 2M1
J2S 2M2
J2S 2M3
J2S 2M4
J2S 2M5
J2S 2M6
J2S 2M7
J2S 2M8
J2S 2M9
J2S 2N1
J2S 2N2
J2S 2N3
J2S 2N4
J2S 2N6
J2S 2N7
J2S 2N8
J2S 2P1
J2S 2P2
J2S 2P3
J2S 2P4
J2S 2P5
J2S 2P6
J2S 2P7
J2S 2P8
J2S 2P9
J2S 2R1
J2S 2R2
J2S 2R3
J2S 2R4
J2S 2R5
J2S 2R6
J2S 2R7
J2S 2R8
J2S 2R9
J2S 2S1
J2S 2S2
J2S 2S3
J2S 2S4
J2S 2S5
J2S 2S6
J2S 2S7
J2S 2S8
J2S 2S9
J2S 2T2
J2S 2T3
J2S 2T4
J2S 2T5
J2S 2T6
J2S 2T7
J2S 2T8
J2S 2T9
J2S 2V1
J2S 2V2
J2S 2V3
J2S 2V4
J2S 2V5
J2S 2V6
J2S 2V7
J2S 2V8
J2S 2V9
J2S 2W1
J2S 2W2
J2S 2W4
J2S 2W5
J2S 2W6
J2S 2W7
J2S 2W8
J2S 2W9
J2S 2X1
J2S 2X2
J2S 2X3
J2S 2X4
J2S 2X5
J2S 2X6
J2S 2X7
J2S 2X8
J2S 2X9
J2S 2Y1
J2S 2Y2
J2S 2Y3
J2S 2Y4
J2S 2Y5
J2S 2Y6
J2S 2Y8
J2S 2Y9
J2S 2Z1
J2S 2Z2
J2S 2Z3
J2S 2Z4
J2S 2Z5
J2S 2Z6
J2S 2Z7
J2S 2Z8
J2S 2Z9
J2S 3A1
J2S 3A2
J2S 3A3
J2S 3A4
J2S 3A5
J2S 3A6
J2S 3A7
J2S 3A8
J2S 3A9
J2S 3B1
J2S 3B2
J2S 3B3
J2S 3B4
J2S 3B5
J2S 3B6
J2S 3B7
J2S 3B8
J2S 3B9
J2S 3C1
J2S 3C2
J2S 3C3
J2S 3C4
J2S 3C6
J2S 3C8
J2S 3C9
J2S 3E1
J2S 3E2
J2S 3E3
J2S 3E4
J2S 3E5
J2S 3E6
J2S 3E7
J2S 3E8
J2S 3E9
J2S 3G1
J2S 3G2
J2S 3G3
J2S 3G4
J2S 3G5
J2S 3G6
J2S 3G7
J2S 3G8
J2S 3G9
J2S 3H1
J2S 3H2
J2S 3H3
J2S 3H4
J2S 3H5
J2S 3H6
J2S 3H7
J2S 3H8
J2S 3H9
J2S 3J1
J2S 3J2
J2S 3J3
J2S 3J4
J2S 3J5
J2S 3J6
J2S 3J9
J2S 3K1
J2S 3K3
J2S 3K4
J2S 3K5
J2S 3K6
J2S 3K7
J2S 3K9
J2S 3L1
J2S 3L2
J2S 3L3
J2S 3L6
J2S 3L7
J2S 3L9
J2S 3M1
J2S 3M2
J2S 3M3
J2S 3M4
J2S 3M5
J2S 3M6
J2S 3M7
J2S 3M8
J2S 3M9
J2S 3N1
J2S 3N2
J2S 3N3
J2S 3N4
J2S 3N5
J2S 3N6
J2S 3N7
J2S 3N8
J2S 3N9
J2S 3P1
J2S 3P2
J2S 3P3
J2S 3P5
J2S 3P6
J2S 3P8
J2S 3P9
J2S 3R1
J2S 3R2
J2S 3R3
J2S 3R4
J2S 3R5
J2S 3R6
J2S 3R7
J2S 3R8
J2S 3R9
J2S 3S1
J2S 3S2
J2S 3S3
J2S 3S4
J2S 3S5
J2S 3S6
J2S 3S7
J2S 3S8
J2S 3S9
J2S 3T1
J2S 3T2
J2S 3T3
J2S 3T4
J2S 3T5
J2S 3T6
J2S 3T7
J2S 3T8
J2S 3T9
J2S 3V1
J2S 3V2
J2S 3V3
J2S 3V4
J2S 3V5
J2S 3V6
J2S 3V7
J2S 3V8
J2S 3V9
J2S 3W1
J2S 3W2
J2S 3W3
J2S 3W4
J2S 3W5
J2S 3W6
J2S 3W7
J2S 3W8
J2S 3W9
J2S 3X1
J2S 3X2
J2S 3X4
J2S 3X5
J2S 3X6
J2S 3X7
J2S 3X8
J2S 3X9
J2S 3Y1
J2S 3Y2
J2S 3Y3
J2S 3Y4
J2S 3Y5
J2S 3Y6
J2S 3Y7
J2S 3Y8
J2S 3Y9
J2S 3Z1
J2S 3Z2
J2S 3Z3
J2S 3Z4
J2S 3Z5
J2S 3Z6
J2S 3Z7
J2S 3Z8
J2S 3Z9
J2S 4A1
J2S 4A2
J2S 4A3
J2S 4A4
J2S 4A5
J2S 4A6
J2S 4A7
J2S 4A8
J2S 4A9
J2S 4B1
J2S 4B2
J2S 4B3
J2S 4B4
J2S 4B5
J2S 4B6
J2S 4B7
J2S 4B8
J2S 4B9
J2S 4C1
J2S 4C2
J2S 4C3
J2S 4C4
J2S 4C5
J2S 4C6
J2S 4C7
J2S 4C8
J2S 4C9
J2S 4E1
J2S 4E2
J2S 4E3
J2S 4E4
J2S 4E5
J2S 4E6
J2S 4E7
J2S 4E8
J2S 4E9
J2S 4G1
J2S 4G2
J2S 4G3
J2S 4G5
J2S 4G6
J2S 4G7
J2S 4G8
J2S 4G9
J2S 4H1
J2S 4H2
J2S 4H3
J2S 4H5
J2S 4H6
J2S 4H7
J2S 4H8
J2S 4H9
J2S 4J1
J2S 4J2
J2S 4J3
J2S 4J4
J2S 4J5
J2S 4J6
J2S 4J7
J2S 4J8
J2S 4J9
J2S 4K1
J2S 4K2
J2S 4K3
J2S 4K4
J2S 4K5
J2S 4K6
J2S 4K7
J2S 4K8
J2S 4K9
J2S 4L1
J2S 4L2
J2S 4L3
J2S 4L4
J2S 4L5
J2S 4L6
J2S 4L7
J2S 4L8
J2S 4L9
J2S 4M1
J2S 4M2
J2S 4M3
J2S 4M5
J2S 4M6
J2S 4M7
J2S 4M8
J2S 4M9
J2S 4N1
J2S 4N2
J2S 4N3
J2S 4N4
J2S 4N5
J2S 4N6
J2S 4N7
J2S 4N9
J2S 4P1
J2S 4P2
J2S 4P3
J2S 4P4
J2S 4P5
J2S 4P6
J2S 4P7
J2S 4P8
J2S 4P9
J2S 4R1
J2S 4R2
J2S 4R3
J2S 4R4
J2S 4R5
J2S 4R6
J2S 4R7
J2S 4R8
J2S 4R9
J2S 4S1
J2S 4S2
J2S 4S3
J2S 4S4
J2S 4S5
J2S 4S6
J2S 4S7
J2S 4S8
J2S 4S9
J2S 4T1
J2S 4T2
J2S 4T3
J2S 4T4
J2S 4T5
J2S 4T6
J2S 4T7
J2S 4T8
J2S 4T9
J2S 4V1
J2S 4V3
J2S 4V4
J2S 4V6
J2S 4V9
J2S 4W1
J2S 4W2
J2S 4W5
J2S 4W6
J2S 4W7
J2S 4W8
J2S 4W9
J2S 4X1
J2S 4X2
J2S 4X3
J2S 4X4
J2S 4X5
J2S 4X6
J2S 4X7
J2S 4X8
J2S 4X9
J2S 4Y1
J2S 4Y2
J2S 4Y3
J2S 4Y4
J2S 4Y5
J2S 4Y6
J2S 4Y8
J2S 4Y9
J2S 4Z1
J2S 4Z2
J2S 4Z3
J2S 4Z4
J2S 4Z5
J2S 4Z6
J2S 4Z7
J2S 4Z8
J2S 5A1
J2S 5A2
J2S 5A3
J2S 5A5
J2S 5A6
J2S 5A7
J2S 5A8
J2S 5A9
J2S 5B1
J2S 5B2
J2S 5B3
J2S 5B4
J2S 5B5
J2S 5B6
J2S 5B7
J2S 5B8
J2S 5B9
J2S 5C1
J2S 5C2
J2S 5C3
J2S 5C4
J2S 5C5
J2S 5C6
J2S 5C8
J2S 5C9
J2S 5E1
J2S 5E2
J2S 5E3
J2S 5E4
J2S 5E5
J2S 5E6
J2S 5E7
J2S 5E8
J2S 5E9
J2S 5G1
J2S 5G2
J2S 5G3
J2S 5G4
J2S 5G5
J2S 5G6
J2S 5G7
J2S 5G9
J2S 5H2
J2S 5H3
J2S 5H4
J2S 5H5
J2S 5H6
J2S 5H7
J2S 5H8
J2S 5H9
J2S 5J1
J2S 5J2
J2S 5J3
J2S 5J4
J2S 5J5
J2S 5J6
J2S 5J7
J2S 5J8
J2S 5J9
J2S 5K1
J2S 5K2
J2S 5K3
J2S 5K4
J2S 5K6
J2S 5K7
J2S 5K8
J2S 5K9
J2S 5L1
J2S 5L2
J2S 5L3
J2S 5L4
J2S 5L5
J2S 5L6
J2S 5L7
J2S 5L8
J2S 5L9
J2S 5M1
J2S 5M2
J2S 5M3
J2S 5M4
J2S 5M5
J2S 5M6
J2S 5M7
J2S 5M8
J2S 5M9
J2S 5N1
J2S 5N2
J2S 5N3
J2S 5N4
J2S 5N5
J2S 5N6
J2S 5N7
J2S 5N8
J2S 5N9
J2S 5P1
J2S 5P2
J2S 5P3
J2S 5P4
J2S 5P5
J2S 5P6
J2S 5P7
J2S 5P8
J2S 5P9
J2S 5R1
J2S 5R2
J2S 5R3
J2S 5R4
J2S 5R5
J2S 5R6
J2S 5R7
J2S 5R8
J2S 5R9
J2S 5S1
J2S 5S2
J2S 5S3
J2S 5S4
J2S 5S5
J2S 5S6
J2S 5S7
J2S 5S8
J2S 5S9
J2S 5T1
J2S 5T2
J2S 5T3
J2S 5T4
J2S 5T5
J2S 5T6
J2S 5T7
J2S 5T8
J2S 5T9
J2S 5V1
J2S 5V2
J2S 5V3
J2S 5V4
J2S 5V5
J2S 5V6
J2S 5V7
J2S 5V9
J2S 5W1
J2S 5W2
J2S 5W3
J2S 5W4
J2S 5W5
J2S 5W6
J2S 5W7
J2S 5W8
J2S 5W9
J2S 5X1
J2S 5X2
J2S 5X3
J2S 5X4
J2S 5X5
J2S 5X6
J2S 5X7
J2S 5X8
J2S 5X9
J2S 5Y1
J2S 5Y2
J2S 5Y3
J2S 5Y4
J2S 5Y5
J2S 5Y6
J2S 5Y7
J2S 5Y8
J2S 5Y9
J2S 5Z1
J2S 5Z2
J2S 5Z3
J2S 5Z4
J2S 5Z5
J2S 5Z6
J2S 5Z7
J2S 5Z8
J2S 5Z9
J2S 6A1
J2S 6A2
J2S 6A3
J2S 6A4
J2S 6A5
J2S 6A6
J2S 6A7
J2S 6A8
J2S 6A9
J2S 6B1
J2S 6B2
J2S 6B4
J2S 6B5
J2S 6B6
J2S 6B7
J2S 6B8
J2S 6B9
J2S 6C1
J2S 6C2
J2S 6C3
J2S 6C4
J2S 6C5
J2S 6C6
J2S 6C7
J2S 6C8
J2S 6C9
J2S 6E1
J2S 6E2
J2S 6E3
J2S 6E4
J2S 6E5
J2S 6E6
J2S 6E8
J2S 6E9
J2S 6G1
J2S 6G3
J2S 6G4
J2S 6G5
J2S 6G6
J2S 6G7
J2S 6G8
J2S 6G9
J2S 6H1
J2S 6H2
J2S 6H3
J2S 6H4
J2S 6H5
J2S 6H6
J2S 6H7
J2S 6H8
J2S 6H9
J2S 6J1
J2S 6J2
J2S 6J3
J2S 6J4
J2S 6J5
J2S 6J6
J2S 6J7
J2S 6J8
J2S 6J9
J2S 6K1
J2S 6K2
J2S 6K3
J2S 6K4
J2S 6K5
J2S 6K6
J2S 6K7
J2S 6K9
J2S 6L1
J2S 6L2
J2S 6L3
J2S 6L4
J2S 6L5
J2S 6L6
J2S 6L7
J2S 6L9
J2S 6M1
J2S 6M2
J2S 6M3
J2S 6M4
J2S 6M5
J2S 6M6
J2S 6M7
J2S 6M9
J2S 6N1
J2S 6N2
J2S 6N3
J2S 6N4
J2S 6N5
J2S 6N6
J2S 6N8
J2S 6N9
J2S 6P1
J2S 6P2
J2S 6P3
J2S 6P4
J2S 6P5
J2S 6P6
J2S 6P7
J2S 6P8
J2S 6P9
J2S 6R1
J2S 6R2
J2S 6R3
J2S 6R4
J2S 6R5
J2S 6R6
J2S 6R7
J2S 6R8
J2S 6R9
J2S 6S1
J2S 6S2
J2S 6S4
J2S 6S5
J2S 6S6
J2S 6S7
J2S 6S8
J2S 6S9
J2S 6T1
J2S 6T2
J2S 6T3
J2S 6T4
J2S 6T5
J2S 6T6
J2S 6T7
J2S 6T8
J2S 6T9
J2S 6V1
J2S 6V2
J2S 6V3
J2S 6V4
J2S 6V5
J2S 6V6
J2S 6V7
J2S 6V8
J2S 6V9
J2S 6W1
J2S 6W2
J2S 6W3
J2S 6W4
J2S 6W5
J2S 6W6
J2S 6W7
J2S 6W8
J2S 6W9
J2S 6X1
J2S 6X2
J2S 6X3
J2S 6X4
J2S 6X5
J2S 6X6
J2S 6X8
J2S 6X9
J2S 6Y1
J2S 6Y2
J2S 6Y3
J2S 6Y4
J2S 6Y5
J2S 6Y6
J2S 6Y7
J2S 6Y8
J2S 6Y9
J2S 6Z1
J2S 6Z2
J2S 6Z3
J2S 6Z4
J2S 6Z5
J2S 6Z6
J2S 6Z7
J2S 6Z8
J2S 6Z9
J2S 7A1
J2S 7A2
J2S 7A3
J2S 7A4
J2S 7A5
J2S 7A6
J2S 7A7
J2S 7A8
J2S 7A9
J2S 7B1
J2S 7B2
J2S 7B3
J2S 7B4
J2S 7B6
J2S 7B7
J2S 7B8
J2S 7C2
J2S 7C3
J2S 7C4
J2S 7C6
J2S 7C8
J2S 7C9
J2S 7E1
J2S 7E2
J2S 7E3
J2S 7E4
J2S 7E5
J2S 7E6
J2S 7E7
J2S 7E8
J2S 7E9
J2S 7G1
J2S 7G2
J2S 7G3
J2S 7G4
J2S 7G5
J2S 7G6
J2S 7G7
J2S 7G8
J2S 7G9
J2S 7H1
J2S 7H2
J2S 7H3
J2S 7H4
J2S 7H5
J2S 7H6
J2S 7H7
J2S 7H8
J2S 7H9
J2S 7J1
J2S 7J2
J2S 7J3
J2S 7J4
J2S 7J5
J2S 7J6
J2S 7J7
J2S 7J8
J2S 7J9
J2S 7K1
J2S 7K2
J2S 7K3
J2S 7K5
J2S 7K6
J2S 7K7
J2S 7K8
J2S 7K9
J2S 7L1
J2S 7L2
J2S 7L3
J2S 7L4
J2S 7L5
J2S 7L6
J2S 7L7
J2S 7L8
J2S 7L9
J2S 7M1
J2S 7M2
J2S 7M3
J2S 7M4
J2S 7M5
J2S 7M6
J2S 7M7
J2S 7M8
J2S 7M9
J2S 7N1
J2S 7N2
J2S 7N3
J2S 7N4
J2S 7N5
J2S 7N6
J2S 7N7
J2S 7N8
J2S 7N9
J2S 7P1
J2S 7P2
J2S 7P3
J2S 7P4
J2S 7P5
J2S 7P6
J2S 7P7
J2S 7P9
J2S 7R1
J2S 7R2
J2S 7R3
J2S 7R4
J2S 7R5
J2S 7R6
J2S 7R7
J2S 7R8
J2S 7R9
J2S 7S1
J2S 7S2
J2S 7S3
J2S 7S4
J2S 7S5
J2S 7S6
J2S 7S7
J2S 7S8
J2S 7S9
J2S 7T1
J2S 7T2
J2S 7T3
J2S 7T4
J2S 7T5
J2S 7T6
J2S 7T7
J2S 7T8
J2S 7T9
J2S 7V1
J2S 7V2
J2S 7V3
J2S 7V4
J2S 7V5
J2S 7V6
J2S 7V7
J2S 7V8
J2S 7V9
J2S 7W1
J2S 7W2
J2S 7W3
J2S 7W4
J2S 7W5
J2S 7W6
J2S 7W7
J2S 7W8
J2S 7W9
J2S 7X1
J2S 7X2
J2S 7X3
J2S 7X4
J2S 7X5
J2S 7X6
J2S 7X7
J2S 7X8
J2S 7X9
J2S 7Y2
J2S 7Y3
J2S 7Y4
J2S 7Y5
J2S 7Y6
J2S 7Y7
J2S 7Y8
J2S 7Y9
J2S 7Z1
J2S 7Z2
J2S 7Z3
J2S 7Z4
J2S 7Z5
J2S 7Z6
J2S 7Z7
J2S 7Z8
J2S 7Z9
J2S 8A1
J2S 8A2
J2S 8A3
J2S 8A5
J2S 8A6
J2S 8A7
J2S 8A8
J2S 8A9
J2S 8B1
J2S 8B2
J2S 8B3
J2S 8B4
J2S 8B5
J2S 8B6
J2S 8B7
J2S 8B8
J2S 8B9
J2S 8C1
J2S 8C2
J2S 8C3
J2S 8C4
J2S 8C5
J2S 8C6
J2S 8C7
J2S 8C8
J2S 8C9
J2S 8E1
J2S 8E3
J2S 8E4
J2S 8E5
J2S 8E6
J2S 8E8
J2S 8G2
J2S 8G5
J2S 8G8
J2S 8G9
J2S 8H1
J2S 8H2
J2S 8H3
J2S 8H4
J2S 8H5
J2S 8H8
J2S 8H9
J2S 8J1
J2S 8J2
J2S 8J3
J2S 8J4
J2S 8J5
J2S 8J6
J2S 8J7
J2S 8J8
J2S 8J9
J2S 8K1
J2S 8K2
J2S 8K4
J2S 8K5
J2S 8K6
J2S 8K7
J2S 8K8
J2S 8K9
J2S 8L1
J2S 8L2
J2S 8L3
J2S 8L4
J2S 8L5
J2S 8L6
J2S 8L7
J2S 8L8
J2S 8L9
J2S 8M1
J2S 8M2
J2S 8M3
J2S 8M4
J2S 8M5
J2S 8M6
J2S 8M7
J2S 8M8
J2S 8M9
J2S 8N1
J2S 8N2
J2S 8N3
J2S 8N4
J2S 8N5
J2S 8N6
J2S 8N7
J2S 8N8
J2S 8N9
J2S 8P1
J2S 8P2
J2S 8P3
J2S 8P4
J2S 8P5
J2S 8P6
J2S 8P7
J2S 8P8
J2S 8P9
J2S 8R1
J2S 8R2
J2S 8R3
J2S 8R4
J2S 8R5
J2S 8R6
J2S 8R7
J2S 8R8
J2S 8R9
J2S 8S1
J2S 8S2
J2S 8S3
J2S 8S4
J2S 8S5
J2S 8S6
J2S 8S7
J2S 8S8
J2S 8T1
J2S 8T2
J2S 8T3
J2S 8T4
J2S 8T5
J2S 8T6
J2S 8T7
J2S 8T8
J2S 8T9
J2S 8V1
J2S 8V2
J2S 8V3
J2S 8V5
J2S 8V6
J2S 8V7
J2S 8V8
J2S 8V9
J2S 8W1
J2S 8W2
J2S 8W3
J2S 8W4
J2S 8W5
J2S 8W6
J2S 8W7
J2S 8W9
J2S 8X1
J2S 8X2
J2S 8X3
J2S 8X4
J2S 8X5
J2S 8X6
J2S 8X7
J2S 8X8
J2S 8X9
J2S 8Y1
J2S 8Y2
J2S 8Y3
J2S 8Y4
J2S 8Y5
J2S 8Y6
J2S 8Y7
J2S 8Y8
J2S 8Y9
J2S 8Z1
J2S 8Z2
J2S 8Z3
J2S 8Z4
J2S 8Z6
J2S 8Z7
J2S 8Z8
J2S 8Z9
J2S 9A1
J2S 9A2
J2S 9A3
J2S 9A4
J2S 9A5
J2S 9A6
J2S 9A7
J2S 9A8
J2S 9A9
J2S 9B1
J2S 9B2
J2S 9B3
J2S 9B4
J2S 9B5
J2S 9B6
J2S 9B7
J2S 9B8
J2S 9B9
J2S 9C1
J2S 9C2
J2S 9C3
J2S 9C4
J2S 9C5
J2S 9C6
J2S 9C7
J2S 9C8
J2S 9C9
J2S 9E1
J2S 9E2
J2S 9E3
J2S 9E4
J2S 9E5
J2S 9E6
J2S 9E7
J2S 9E8
J2S 9E9
J2S 9G1
J2S 9G2
J2S 9G3
J2T 0A1
J2T 0A2
J2T 0A3
J2T 0A4
J2T 0A5
J2T 0A6
J2T 0A7
J2T 0A8
J2T 0A9
J2T 0B1
J2T 0B2
J2T 0B3
J2T 0B4
J2T 1A1
J2T 1A2
J2T 1A3
J2T 1A4
J2T 1A5
J2T 1A6
J2T 1A7
J2T 1A8
J2T 1A9
J2T 1B1
J2T 1B2
J2T 1B3
J2T 1B4
J2T 1B5
J2T 1B6
J2T 1B7
J2T 1B8
J2T 1B9
J2T 1C1
J2T 1C2
J2T 1C3
J2T 1C4
J2T 1C5
J2T 1C6
J2T 1C7
J2T 1C8
J2T 1C9
J2T 1E1
J2T 1E2
J2T 1E3
J2T 1E4
J2T 1E5
J2T 1E6
J2T 1E7
J2T 1E8
J2T 1E9
J2T 1G1
J2T 1G2
J2T 1G3
J2T 1G4
J2T 1G5
J2T 1G6
J2T 1G7
J2T 1G8
J2T 1G9
J2T 1H1
J2T 1H2
J2T 1H3
J2T 1H4
J2T 1H5
J2T 1H6
J2T 1H7
J2T 1H8
J2T 1H9
J2T 1J1
J2T 1J2
J2T 1J3
J2T 1J4
J2T 1J5
J2T 1J6
J2T 1J7
J2T 1J8
J2T 1K1
J2T 1K2
J2T 1K3
J2T 1K4
J2T 1K5
J2T 1K6
J2T 1K7
J2T 1K8
J2T 1K9
J2T 1L3
J2T 1L4
J2T 1L5
J2T 1L6
J2T 1L7
J2T 1L8
J2T 1L9
J2T 1M1
J2T 1M2
J2T 1M3
J2T 1M4
J2T 1M5
J2T 1M6
J2T 1M7
J2T 1M8
J2T 1M9
J2T 1N2
J2T 1N3
J2T 1N4
J2T 1N5
J2T 1N6
J2T 1N7
J2T 1N8
J2T 1N9
J2T 1P1
J2T 1P2
J2T 1P3
J2T 1P4
J2T 1P5
J2T 1P6
J2T 1P7
J2T 1P8
J2T 1P9
J2T 1R1
J2T 1R2
J2T 1R3
J2T 1R4
J2T 1R5
J2T 1R6
J2T 1R7
J2T 1R8
J2T 1R9
J2T 1S1
J2T 1S2
J2T 1S3
J2T 1S4
J2T 1S5
J2T 1S6
J2T 1S7
J2T 1S8
J2T 1S9
J2T 1T1
J2T 1T2
J2T 1T3
J2T 1T4
J2T 1T5
J2T 1T6
J2T 1T7
J2T 1T8
J2T 1T9
J2T 1V1
J2T 1V2
J2T 1V3
J2T 1V4
J2T 1V5
J2T 1V7
J2T 1V8
J2T 1V9
J2T 1W1
J2T 1W2
J2T 1W3
J2T 1W4
J2T 1W5
J2T 1W6
J2T 1W7
J2T 1W8
J2T 1W9
J2T 1X1
J2T 1X2
J2T 1X3
J2T 1X4
J2T 1X5
J2T 1X6
J2T 1X7
J2T 1X8
J2T 1X9
J2T 1Y1
J2T 1Y2
J2T 1Y3
J2T 1Y4
J2T 1Y5
J2T 1Y6
J2T 1Y7
J2T 1Y8
J2T 1Y9
J2T 1Z1
J2T 1Z2
J2T 1Z3
J2T 1Z4
J2T 1Z5
J2T 1Z6
J2T 1Z7
J2T 1Z8
J2T 1Z9
J2T 2A1
J2T 2A2
J2T 2A3
J2T 2A4
J2T 2A5
J2T 2A6
J2T 2A7
J2T 2A8
J2T 2A9
J2T 2B1
J2T 2B2
J2T 2B3
J2T 2B4
J2T 2B5
J2T 2B6
J2T 2B7
J2T 2B8
J2T 2B9
J2T 2C1
J2T 2C2
J2T 2C3
J2T 2C4
J2T 2C5
J2T 2C6
J2T 2C7
J2T 2C8
J2T 2C9
J2T 2E1
J2T 2E2
J2T 2E3
J2T 2E4
J2T 2E5
J2T 2E6
J2T 2E7
J2T 2E8
J2T 2E9
J2T 2G1
J2T 2G3
J2T 2G4
J2T 2G7
J2T 2G8
J2T 2G9
J2T 2H1
J2T 2H3
J2T 2H4
J2T 2H5
J2T 2H6
J2T 2H7
J2T 2H8
J2T 2H9
J2T 2J1
J2T 2J2
J2T 2J3
J2T 2J4
J2T 2J7
J2T 2J8
J2T 2K2
J2T 2K3
J2T 2K4
J2T 2K5
J2T 2K6
J2T 2K7
J2T 2K8
J2T 2K9
J2T 2L1
J2T 2L2
J2T 2L3
J2T 2L4
J2T 2L5
J2T 2L6
J2T 2L7
J2T 2L8
J2T 2L9
J2T 2M1
J2T 2M2
J2T 2M3
J2T 2M4
J2T 2M5
J2T 2M6
J2T 2M7
J2T 2M8
J2T 2M9
J2T 2N1
J2T 2N2
J2T 2N3
J2T 2N4
J2T 2N5
J2T 2N6
J2T 2N7
J2T 2N8
J2T 2N9
J2T 2P1
J2T 2P2
J2T 2P3
J2T 2P4
J2T 2P5
J2T 2P6
J2T 2P7
J2T 2P8
J2T 2P9
J2T 2R1
J2T 2R2
J2T 2R3
J2T 2R4
J2T 2R5
J2T 2R6
J2T 2R7
J2T 2R8
J2T 2R9
J2T 2S1
J2T 2S2
J2T 2S3
J2T 2S4
J2T 2S5
J2T 2S6
J2T 2S7
J2T 2S8
J2T 2S9
J2T 2T2
J2T 2T3
J2T 2T4
J2T 2T5
J2T 2T6
J2T 2T7
J2T 2T8
J2T 2V1
J2T 2V2
J2T 2V3
J2T 2V4
J2T 2V5
J2T 2V6
J2T 2V7
J2T 2V8
J2T 2V9
J2T 2W1
J2T 2W2
J2T 2W3
J2T 2W4
J2T 2W5
J2T 2W6
J2T 2W7
J2T 2W8
J2T 2W9
J2T 2X1
J2T 2X2
J2T 2X3
J2T 2X4
J2T 2X5
J2T 2X6
J2T 2X7
J2T 2X8
J2T 2X9
J2T 2Y1
J2T 2Y2
J2T 2Y3
J2T 2Y4
J2T 2Y5
J2T 2Y6
J2T 2Y7
J2T 2Y8
J2T 2Y9
J2T 2Z1
J2T 2Z2
J2T 2Z3
J2T 2Z4
J2T 2Z5
J2T 2Z6
J2T 2Z7
J2T 3A1
J2T 3A2
J2T 3A3
J2T 3A4
J2T 3A5
J2T 3A6
J2T 3A7
J2T 3A8
J2T 3A9
J2T 3B1
J2T 3B2
J2T 3B3
J2T 3B4
J2T 3B5
J2T 3B6
J2T 3B7
J2T 3B8
J2T 3B9
J2T 3C1
J2T 3C2
J2T 3C3
J2T 3C4
J2T 3C5
J2T 3C6
J2T 3C7
J2T 3C8
J2T 3C9
J2T 3E1
J2T 3E2
J2T 3E3
J2T 3E4
J2T 3E5
J2T 3E6
J2T 3E7
J2T 3E8
J2T 3E9
J2T 3G1
J2T 3G2
J2T 3G3
J2T 3G4
J2T 3G5
J2T 3G6
J2T 3G7
J2T 3G8
J2T 3G9
J2T 3H1
J2T 3H2
J2T 3H3
J2T 3H4
J2T 3H5
J2T 3H6
J2T 3H7
J2T 3H8
J2T 3H9
J2T 3J1
J2T 3J2
J2T 3J3
J2T 3J4
J2T 3J5
J2T 3J6
J2T 3J7
J2T 3J9
J2T 3K1
J2T 3K2
J2T 3K3
J2T 3K4
J2T 3K5
J2T 3K6
J2T 3K7
J2T 3K8
J2T 3K9
J2T 3L1
J2T 3L2
J2T 3L3
J2T 3L4
J2T 3L5
J2T 3L6
J2T 3L7
J2T 3L8
J2T 3L9
J2T 3M1
J2T 3M2
J2T 3M3
J2T 3M4
J2T 3M5
J2T 3M6
J2T 3M7
J2T 3M8
J2T 3M9
J2T 3N1
J2T 3N2
J2T 3N3
J2T 3N4
J2T 3N5
J2T 3N6
J2T 3N7
J2T 3N8
J2T 3N9
J2T 3P1
J2T 3P2
J2T 3P3
J2T 3P4
J2T 3P5
J2T 3P6
J2T 3P7
J2T 3P8
J2T 3P9
J2T 3R1
J2T 3R2
J2T 3R3
J2T 3R4
J2T 3R5
J2T 3R6
J2T 3R7
J2T 3R8
J2T 3R9
J2T 3S1
J2T 3S2
J2T 3S3
J2T 3S4
J2T 3S5
J2T 3S6
J2T 3S7
J2T 3S8
J2T 3S9
J2T 3T1
J2T 3T2
J2T 3T3
J2T 3T4
J2T 3T5
J2T 3T6
J2T 3T7
J2T 3T8
J2T 3T9
J2T 3V1
J2T 3V2
J2T 3V3
J2T 3V4
J2T 3V5
J2T 3V6
J2T 3V7
J2T 3V8
J2T 3V9
J2T 3W1
J2T 3W2
J2T 3W3
J2T 3W4
J2T 3W5
J2T 3W6
J2T 3W7
J2T 3W8
J2T 3X1
J2T 3X2
J2T 3X3
J2T 3X4
J2T 3X5
J2T 3X6
J2T 3X7
J2T 3X8
J2T 3X9
J2T 3Y1
J2T 3Y2
J2T 3Y3
J2T 3Y4
J2T 3Y5
J2T 3Y6
J2T 3Y7
J2T 3Y8
J2T 3Y9
J2T 3Z1
J2T 3Z2
J2T 3Z3
J2T 3Z4
J2T 3Z5
J2T 3Z6
J2T 3Z7
J2T 3Z8
J2T 3Z9
J2T 4A1
J2T 4A2
J2T 4A3
J2T 4A4
J2T 4A5
J2T 4A6
J2T 4A7
J2T 4A8
J2T 4A9
J2T 4B1
J2T 4B2
J2T 4B3
J2T 4B4
J2T 4B5
J2T 4B6
J2T 4B7
J2T 4B8
J2T 4B9
J2T 4C1
J2T 4C2
J2T 4C3
J2T 4C4
J2T 4C5
J2T 4C6
J2T 4C7
J2T 4C8
J2T 4C9
J2T 4E1
J2T 4E2
J2T 4E3
J2T 4E4
J2T 4E5
J2T 4E6
J2T 4E7
J2T 4E8
J2T 4E9
J2T 4G1
J2T 4G3
J2T 4G4
J2T 4G5
J2T 4G6
J2T 4G7
J2T 4G8
J2T 4G9
J2T 4H1
J2T 4H2
J2T 4H3
J2T 4H4
J2T 4H5
J2T 4H6
J2T 4H7
J2T 4H8
J2T 4H9
J2T 4J1
J2T 4J2
J2T 4J3
J2T 4J4
J2T 4J5
J2T 4J6
J2T 4J7
J2T 4J8
J2T 4J9
J2T 4K1
J2T 4K2
J2T 4K3
J2T 4K4
J2T 4K5
J2T 4K6
J2T 4K7
J2T 4K8
J2T 4K9
J2T 4L1
J2T 4L3
J2T 4L4
J2T 4L5
J2T 4L6
J2T 4L7
J2T 4L8
J2T 4L9
J2T 4M1
J2T 4M2
J2T 4M3
J2T 4M4
J2T 4M5
J2T 4M6
J2T 4M7
J2T 4M8
J2T 4M9
J2T 4N1
J2T 4N2
J2T 4N3
J2T 4N4
J2T 4N5
J2T 4N6
J2T 4N7
J2T 4N8
J2T 4N9
J2T 4P1
J2T 4P2
J2T 4P3
J2T 4P4
J2T 4P5
J2T 4P6
J2T 4P7
J2T 4P8
J2T 4P9
J2T 4R1
J2T 4R2
J2T 4R3
J2T 4R4
J2T 4R5
J2T 4R6
J2T 4R7
J2T 4R8
J2T 4R9
J2T 4S1
J2T 4S4
J2T 4S5
J2T 4S6
J2T 4S7
J2T 4S8
J2T 4S9
J2T 4T1
J2T 4T2
J2T 4T3
J2T 4T4
J2T 4T5
J2T 4T6
J2T 4T7
J2T 4T8
J2T 4T9
J2T 4V1
J2T 4V2
J2T 4V3
J2T 4V4
J2T 4V5
J2T 4V6
J2T 4V8
J2T 4V9
J2T 4W1
J2T 4W4
J2T 4W5
J2T 4W7
J2T 4W8
J2T 4W9
J2T 4X1
J2T 4X4
J2T 4X6
J2T 4X8
J2T 4Y3
J2T 4Y4
J2T 4Y5
J2T 4Y6
J2T 4Y7
J2T 4Y8
J2T 4Y9
J2T 4Z1
J2T 4Z2
J2T 4Z3
J2T 4Z4
J2T 4Z5
J2T 4Z6
J2T 4Z7
J2T 4Z8
J2T 4Z9
J2T 5A1
J2T 5A2
J2T 5A3
J2T 5A4
J2T 5A5
J2T 5A6
J2T 5A7
J2T 5A8
J2T 5A9
J2T 5B1
J2T 5B2
J2T 5B3
J2T 5B4
J2T 5B5
J2T 5B6
J2T 5B7
J2T 5B8
J2T 5B9
J2T 5C1
J2T 5C2
J2T 5C3
J2T 5C4
J2T 5C5
J2T 5C6
J2T 5C7
J2T 5C8
J2T 5C9
J2T 5E1
J2T 5E2
J2T 5E3
J2T 5E4
J2T 5E5
J2T 5E6
J2T 5E7
J2T 5E8
J2T 5E9
J2T 5G1
J2T 5G2
J2T 5G3
J2T 5G4
J2T 5G5
J2T 5G6
J2T 5G7
J2T 5G8
J2T 5G9
J2T 5H1
J2T 5H2
J2T 5H3
J2T 5H4
J2T 5H5
J2T 5H7
J2T 5H8
J2T 5H9
J2T 5J1
J2T 5J4
J2T 5J5
J2T 5J6
J2T 5J7
J2T 5J8
J2T 5J9
J2T 5K1
J2T 5K2
J2T 5K3
J2T 5K4
J2T 5K5
J2T 5K6
J2T 5K7
J2T 5K8
J2T 5K9
J2T 5L1
J2T 5L2
J2T 5L3
J2T 5L4
J2T 5L5
J2T 5L6""".strip().split("\n")
import urllib.parse, xml.dom.minidom, urllib.request
def AddressComplete_Interactive_Find_v2_10(search):

    LastId = "CA|CP|ENG|" + search.split(" ")[1] + "-" + search.split(" ")[0] 
    SearchTerm = ""
    Key = API
    SearchFor = "Everything"
    Country = "CAN"
    LanguagePreference = "EN"
    MaxSuggestions = 1000
    MaxResults = 1000

    #Build the url
    requestUrl = "http://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/Find/v2.10/xmla.ws?"
    requestUrl += "&" +  urllib.parse.urlencode({"Key":Key})
    requestUrl += "&" +  urllib.parse.urlencode({"SearchTerm":SearchTerm})
    requestUrl += "&" +  urllib.parse.urlencode({"LastId":LastId})
    requestUrl += "&" +  urllib.parse.urlencode({"SearchFor":SearchFor})
    requestUrl += "&" +  urllib.parse.urlencode({"Country":Country})
    requestUrl += "&" +  urllib.parse.urlencode({"LanguagePreference":LanguagePreference})
    requestUrl += "&" +  urllib.parse.urlencode({"MaxSuggestions":MaxSuggestions})
    requestUrl += "&" +  urllib.parse.urlencode({"MaxResults":MaxResults})
    print(requestUrl)
    exit()
    #Get the data
    dataDoc = xml.dom.minidom.parseString(urllib.request.urlopen(requestUrl).read())

    #Get references to the schema and data
    schemaNodes = dataDoc.getElementsByTagName("Column")
    dataNotes = dataDoc.getElementsByTagName("Row")


    #Work though the items in the response
    results = []
    for dataNode in dataNotes:
        rowData = dict()
        for schemaNode in schemaNodes:
            key = schemaNode.attributes["Name"].value
            value = dataNode.attributes[key].value
            rowData[key] = value
            results.append(rowData)
    print(results)
    exit()
    return results

    #FYI: The output is an array of key value pairs, the keys being:
    #Id
    #Text
    #Highlight
    #Cursor
    #Description
    #Next

import json, os, time
outfile = open('data.json', 'w')
outfile.write('[')
start = time.time()
for i in range(len(postalCode)):

        code = postalCode[i]
        postal = {}
        code = code.strip()
        postal[code] = []
        addresse = AddressComplete_Interactive_Find_v2_10(code)
        for e in addresse:
            postal[code].append(e["Text"])
            postal[code] = list(set(postal[code]))
        json.dump(postal, outfile)
        outfile.write(',')
        spent = time.time() - start
        print(len(postalCode) * spent / (i + 1.0) - spent )

outfile.write(']')