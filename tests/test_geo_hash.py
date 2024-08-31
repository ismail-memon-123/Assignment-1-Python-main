from cs5278_assignment_1.geo_hash import GeoHash


class TestGeoHash:
    @staticmethod
    def test_assorted_1d_hashes():
        # If you can get the 1D geohash to pass all of these tests, you should be in
        # good shape to complete the 2D version.

        GeoHash.assert_equals("00000", GeoHash.geo_hash_string(
            GeoHash.LONGITUDE_RANGE[0], GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("00000", GeoHash.geo_hash_string(
            GeoHash.LATITUDE_RANGE[0], GeoHash.LATITUDE_RANGE, 5))
        GeoHash.assert_equals("11111", GeoHash.geo_hash_string(
            GeoHash.LONGITUDE_RANGE[1], GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("11111", GeoHash.geo_hash_string(
            GeoHash.LATITUDE_RANGE[1], GeoHash.LATITUDE_RANGE, 5))
        GeoHash.assert_equals("10000", GeoHash.geo_hash_string(
            0, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("11000", GeoHash.geo_hash_string(
            90.0, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("11100", GeoHash.geo_hash_string(
            135.0, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("11110", GeoHash.geo_hash_string(
            157.5, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("11111", GeoHash.geo_hash_string(
            168.75, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("01111", GeoHash.geo_hash_string(
            -1, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("00111", GeoHash.geo_hash_string(
            -91.0, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("00011", GeoHash.geo_hash_string(
            -136.0, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("00001", GeoHash.geo_hash_string(
            -158.5, GeoHash.LONGITUDE_RANGE, 5))
        GeoHash.assert_equals("00000", GeoHash.geo_hash_string(
            -169.75, GeoHash.LONGITUDE_RANGE, 5))

    @staticmethod
    def test_assorted_2d_hashes():
        GeoHash.assert_equals("0000000000", GeoHash.to_hash_string(
            GeoHash.geo_hash(GeoHash.LATITUDE_RANGE[0], GeoHash.LONGITUDE_RANGE[0], 10)))
        GeoHash.assert_equals("0101010101", GeoHash.to_hash_string(
            GeoHash.geo_hash(GeoHash.LATITUDE_RANGE[0], GeoHash.LONGITUDE_RANGE[1], 10)))
        GeoHash.assert_equals("01010101010", GeoHash.to_hash_string(
            GeoHash.geo_hash(GeoHash.LATITUDE_RANGE[0], GeoHash.LONGITUDE_RANGE[1], 11)))
        GeoHash.assert_equals("01010101010", GeoHash.to_hash_string(
            GeoHash.geo_hash(GeoHash.LATITUDE_RANGE[0], GeoHash.LONGITUDE_RANGE[1], 11)))
        GeoHash.assert_equals("1010101011", GeoHash.to_hash_string(
            GeoHash.geo_hash(GeoHash.LATITUDE_RANGE[1], -158.5, 10)))
        GeoHash.assert_equals("10101010111", GeoHash.to_hash_string(
            GeoHash.geo_hash(GeoHash.LATITUDE_RANGE[1], -158.5, 11)))
        GeoHash.assert_equals("10101010111111", GeoHash.to_hash_string(
            GeoHash.geo_hash(GeoHash.LATITUDE_RANGE[1], -158.5, 14)))
        GeoHash.assert_equals("11111111111111", GeoHash.to_hash_string(
            GeoHash.geo_hash(GeoHash.LATITUDE_RANGE[1], GeoHash.LONGITUDE_RANGE[1], 14)))
