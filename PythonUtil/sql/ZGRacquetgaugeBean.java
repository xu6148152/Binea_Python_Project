package com.zepp.golfsense.data.models;

    import java.io.Serializable;
    import android.content.ContentValues;

    import com.zepp.golfsense.data.models.DataStructs.RacquetgaugeColumns;

    public class ZGRacquetgaugeBean implements Serializable, ZGBean {

    	private static final String TAG = ZGRacquetgaugeBean.class.getSimpleName();
private String "Gauge";
public ZGRacquetgaugeBean() {
"Gauge" = " TEXT(255,0) NOT NULL;
}

public ZGRacquetgaugeBean(ZGRacquetgaugeBean copy) {
"Gauge" = copy."Gauge";
}

@Override
	public ContentValues toContentValues() {
		ContentValues cv = new ContentValues();
cv.put(RacquetgaugeColumns."GAUGE", "Gauge");
return cv;
}

@Override
	public ZGRacquetgaugeBean fromContentValues(ContentValues cv) {
"Gauge" = cv.getAsString(RacquetgaugeColumns."GAUGE");
return this;
}

}

