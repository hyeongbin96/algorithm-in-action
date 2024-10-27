SELECT
    COUNT(FN.FISH_TYPE) AS FISH_COUNT,
    FN.FISH_NAME
FROM
    FISH_NAME_INFO FN
JOIN
    FISH_INFO FI ON FN.FISH_TYPE = FI.FISH_TYPE
GROUP BY
    FN.FISH_NAME
ORDER BY
    FISH_COUNT DESC