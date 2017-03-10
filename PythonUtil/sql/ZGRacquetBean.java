package com.zepp.golfsense.data.models;

    import java.io.Serializable;
    import android.content.ContentValues;

    import com.zepp.golfsense.data.models.DataStructs.RacquetColumns;

    public class ZGRacquetBean implements Serializable, ZGBean {

    	private static final String TAG = ZGRacquetBean.class.getSimpleName();
private int "Model_ID";
private String "Make_Name";
private String "Model_Name";
private int "Type_1";
private int "Type_2";
private double "Length";
private String "Icon";
public ZGRacquetBean() {
"Model_ID" = _ID" int(255,0);
"Make_Name" = Name" TEXT(255,0);
"Model_Name" = _Name" TEXT(255,0);
"Type_1" = 1" int(255,0);
"Type_2" = 2" int(255,0);
"Length" = h" REAL(255,0);
"Icon" = TEXT(255,0);
}

public ZGRacquetBean(ZGRacquetBean copy) {
"Model_ID" = copy."Model_ID";
"Make_Name" = copy."Make_Name";
"Model_Name" = copy."Model_Name";
"Type_1" = copy."Type_1";
"Type_2" = copy."Type_2";
"Length" = copy."Length";
"Icon" = copy."Icon";
}

@Override
	public ContentValues toContentValues() {
		ContentValues cv = new ContentValues();
cv.put(RacquetColumns."MODEL_ID", "Model_ID");
cv.put(RacquetColumns."MAKE_NAME", "Make_Name");
cv.put(RacquetColumns."MODEL_NAME", "Model_Name");
cv.put(RacquetColumns."TYPE_1", "Type_1");
cv.put(RacquetColumns."TYPE_2", "Type_2");
cv.put(RacquetColumns."LENGTH", "Length");
cv.put(RacquetColumns."ICON", "Icon");
return cv;
}

@Override
	public ZGRacquetBean fromContentValues(ContentValues cv) {
"Model_ID" = cv.getAsInteger(RacquetColumns."MODEL_ID");
"Make_Name" = cv.getAsString(RacquetColumns."MAKE_NAME");
"Model_Name" = cv.getAsString(RacquetColumns."MODEL_NAME");
"Type_1" = cv.getAsInteger(RacquetColumns."TYPE_1");
"Type_2" = cv.getAsInteger(RacquetColumns."TYPE_2");
"Length" = cv.getAsDouble(RacquetColumns."LENGTH");
"Icon" = cv.getAsString(RacquetColumns."ICON");
return this;
}

}

