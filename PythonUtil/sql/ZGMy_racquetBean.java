package com.zepp.golfsense.data.models;

    import java.io.Serializable;
    import android.content.ContentValues;

    import com.zepp.golfsense.data.models.DataStructs.My_racquetColumns;

    public class ZGMy_racquetBean implements Serializable, ZGBean {

    	private static final String TAG = ZGMy_racquetBean.class.getSimpleName();
private int "Make_ID";
private int "Model_ID";
private String "Make_Name";
private String "Model_Name";
private int "Type_1";
private int "Type_2";
private double "Length";
private String "Icon";
public ZGMy_racquetBean() {
"Make_ID" = ID" int(255,0);
"Model_ID" = _ID" int(255,0);
"Make_Name" = Name" TEXT(255,0);
"Model_Name" = _Name" TEXT(255,0);
"Type_1" = 1" int(255,0);
"Type_2" = 2" int(255,0);
"Length" = h" REAL(255,0);
"Icon" = TEXT(255,0);
}

public ZGMy_racquetBean(ZGMy_racquetBean copy) {
"Make_ID" = copy."Make_ID";
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
cv.put(My_racquetColumns."MAKE_ID", "Make_ID");
cv.put(My_racquetColumns."MODEL_ID", "Model_ID");
cv.put(My_racquetColumns."MAKE_NAME", "Make_Name");
cv.put(My_racquetColumns."MODEL_NAME", "Model_Name");
cv.put(My_racquetColumns."TYPE_1", "Type_1");
cv.put(My_racquetColumns."TYPE_2", "Type_2");
cv.put(My_racquetColumns."LENGTH", "Length");
cv.put(My_racquetColumns."ICON", "Icon");
return cv;
}

@Override
	public ZGMy_racquetBean fromContentValues(ContentValues cv) {
"Make_ID" = cv.getAsInteger(My_racquetColumns."MAKE_ID");
"Model_ID" = cv.getAsInteger(My_racquetColumns."MODEL_ID");
"Make_Name" = cv.getAsString(My_racquetColumns."MAKE_NAME");
"Model_Name" = cv.getAsString(My_racquetColumns."MODEL_NAME");
"Type_1" = cv.getAsInteger(My_racquetColumns."TYPE_1");
"Type_2" = cv.getAsInteger(My_racquetColumns."TYPE_2");
"Length" = cv.getAsDouble(My_racquetColumns."LENGTH");
"Icon" = cv.getAsString(My_racquetColumns."ICON");
return this;
}

}

