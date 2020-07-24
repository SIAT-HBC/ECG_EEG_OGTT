package demo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Comparator;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.Vector;

public class STQTprogram {

    public void checkfrequency() {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/demo", "root", "");
            Statement statement = conn.createStatement();
            String[] name = {"ecg_morenikeji_control"};
            ResultSet rset = statement.executeQuery("select * from " + name[0] + " order by id");
            TreeMap<Double, Integer> record = new TreeMap<Double, Integer>();
            NumberFormat df = DecimalFormat.getInstance();
            df.setMaximumFractionDigits(2);
            Vector<String> MN = new Vector<String>();
            Vector<String> SD = new Vector<String>();
            double change = 0;
            int counter = 0;
            String segment = "ST";
            while (rset.next()) {
                double glucose = Double.parseDouble(rset.getObject("glucose").toString());
                double num_double = 0;
                if (rset.getObject(segment).toString().equals("----")) {
                    counter++;
                } else {
                    num_double = Double.parseDouble(df.format(Double.parseDouble(rset.getObject(segment).toString())));
                    counter++;
                }
                if (record.containsKey(num_double)) {
                    record.put(num_double, record.get(num_double) + 1);
                } else {
                    record.put(num_double, 1);
                }
                if ((counter % 520) == 0) {//time inteval
                    Map sortedMap = sortByValues(record);
                    Set set = sortedMap.entrySet();
                    Iterator its = set.iterator();
                    int size = sortedMap.size();
                    int itemcounter = 0;
                    int printsize = 9;
                    int frequency = 0;
                    double summation = 0;
                    while (its.hasNext()) {
                        Map.Entry pair = (Map.Entry) its.next();
                        if ((size - ++itemcounter) == printsize) {
                            printsize--;

                            frequency += Integer.parseInt(pair.getValue().toString());
                            summation += Double.parseDouble(pair.getKey().toString()) * Integer.parseInt(pair.getValue().toString());
                           System.out.print(pair.getKey());//10 most occurring values
                        }

                    }
//                    System.out.println(summation);
//                    System.out.println(frequency);

                    double mean = summation / frequency;
                    Iterator it = set.iterator();
                    itemcounter = 0;
                    printsize = 9;
                    double value_bar = 0;
                    while (it.hasNext()) {
                        Map.Entry pair = (Map.Entry) it.next();
                        if ((size - ++itemcounter) == printsize) {
                            printsize--;
//                            System.out.print("Key is: " + pair.getKey() + " and ");
//                            System.out.println("Value is: " + pair.getValue());    
                            value_bar += Integer.parseInt(pair.getValue().toString()) * Math.pow((mean - Double.parseDouble(pair.getKey().toString())), 2);
							System.out.print(pair.getKey());
                        }
                    }

                    double sd = Math.sqrt(value_bar / (frequency - 1));
                    MN.add(String.format("%.3f", mean));
                    SD.add(String.format("%.3f", sd));
//                    System.out.printf("%.3f;%.3f\n", mean, sd);

                } else {
//                    change = glucose;
                }
            }
            for (String s : MN) {
                System.out.print(s + ",");
            }
            System.out.println();
            for (String s : SD) {
                System.out.print(s + ",");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
	
	public static void main(String arg[]) {
        new STQTprogram().checkboxplot();
    }

    public static <K, V extends Comparable<V>> Map<K, V>
            sortByValues(final Map<K, V> map) {
        Comparator<K> valueComparator
                = new Comparator<K>() {
            public int compare(K k1, K k2) {
                int compare
                        = map.get(k1).compareTo(map.get(k2));
                if (compare == 0) {
                    return 1;
                } else {
                    return compare;
                }
            }
        };

        Map<K, V> sortedByValues
                = new TreeMap<K, V>(valueComparator);
        sortedByValues.putAll(map);
        return sortedByValues;
    }
	}