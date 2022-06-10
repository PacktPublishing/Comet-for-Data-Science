package packt.comet;

import ml.comet.experiment.ExperimentBuilder;
import ml.comet.experiment.OnlineExperiment;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        OnlineExperiment experiment = ExperimentBuilder.OnlineExperiment()
                .build();
        experiment.setExperimentName("My experiment");
        experiment.logParameter("batch_size", "500");
        experiment.logMetric("strMetric", 123);
        experiment.end();
    }
}
